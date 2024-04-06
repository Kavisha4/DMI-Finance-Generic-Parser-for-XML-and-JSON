import csv
import json
from pymongo import MongoClient


def json_to_csv(data):
    file_name = "output.csv"
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        # Write header
        writer.writerow(["Table", "Attribute", "Value"])
        # Write rows
        parse_data(writer, data)

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

def process_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # Process JSON data to CSV
    json_to_csv(data)
    
    # Generate metadata
    metadata = generate_metadata(data)
    
    return metadata