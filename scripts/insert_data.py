import csv
from pymongo import MongoClient
import json

# Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://kvsha2002:dbUserPassword@cluster0.rgozber.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['mydatabase']

def json_to_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
       
    file_name = "output.csv"
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        # Write header
        writer.writerow(["Table", "Attribute", "Value"])
        # Write rows
        parse_data(writer, data)
    return file_name

def parse_data(writer, data, parent_section=""):
    for key, value in data.items():
        if isinstance(value, dict):
            if parent_section:
                section = f"{parent_section} - {key}"
            else:
                section = key
            parse_data(writer, value, section)
        elif isinstance(value, list):
            for index, item in enumerate(value, start=1):
                if isinstance(item, dict):
                    parse_data(writer, item, key)
                else:
                    writer.writerow([key, f"Item {index}", item])
        else:
            if parent_section:
                writer.writerow([parent_section, key, value])
            else:
                writer.writerow([key, "", value])

def generate_metadata(data):
    metadata = {}
    metadata["Top-Level"] = list(data.keys())
    generate_metadata_recursive(data, metadata)
    return metadata

def generate_metadata_recursive(data, metadata, parent_section=""):
    for key, value in data.items():
        if isinstance(value, dict):
            if parent_section:
                section = f"{parent_section} - {key}"
            else:
                section = key
            metadata[section] = list(value.keys())
            generate_metadata_recursive(value, metadata, section)
        elif isinstance(value, list):
            for index, item in enumerate(value, start=1):
                if isinstance(item, dict):
                    nested_section = f"{key}"
                    metadata[nested_section] = list(item.keys())
                    generate_metadata_recursive(item, metadata, nested_section)

# File path to JSON data
file_path = "JSON\Erro_Json.json"

# Call the function to convert JSON to CSV
csv_file_path = json_to_csv(file_path)

# Generate metadata
metadata = generate_metadata(json.load(open(file_path)))

# Print metadata
for section, attributes in metadata.items():
    print(section + ":", attributes)

# Insert CSV data into MongoDB
collection_name = "csv_data"
collection = db[collection_name]

with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    csv_data = []
    for row in csv_reader:
        csv_data.append(row)

# Insert metadata into MongoDB
metadata_collection_name = "metadata"
metadata_collection = db[metadata_collection_name]
metadata_collection.insert_one(metadata)

# Insert CSV data into MongoDB
csv_collection_name = "csv_data"
csv_collection = db[csv_collection_name]
csv_collection.insert_many(csv_data)

print("CSV data and metadata stored in MongoDB successfully!")