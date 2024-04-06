import json
import csv

def process_json_file(file_name):
    def json_to_csv(data, section_name):
        file_name = f"{section_name}.csv"
        with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            if isinstance(data[section_name], list) and data[section_name]:
                # Write header
                writer.writerow(data[section_name][0].keys())
                # Write rows
                for item in data[section_name]:
                    writer.writerow(item.values())
            elif isinstance(data[section_name], dict):
                # Write header
                writer.writerow(data[section_name].keys())
                # Write row
                writer.writerow(data[section_name].values())

    def generate_metadata(data):
        metadata = {}
        metadata["top-level"] = list(data.keys())
        for section_name, section_data in data.items():
            if isinstance(section_data, list) and section_data:
                metadata[section_name] = list(section_data[0].keys())
        return metadata

    # Load JSON data from file
    with open(file_name, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    # Get section names dynamically and create CSV files
    sections = [section for section in json_data["JSON-RESPONSE-OBJECT"].keys() if isinstance(json_data["JSON-RESPONSE-OBJECT"][section], list)]
    for section in sections:
        json_to_csv(json_data["JSON-RESPONSE-OBJECT"], section)

    # Generate metadata
    metadata = generate_metadata(json_data["JSON-RESPONSE-OBJECT"])

    # Create a CSV file for non-JSON response object
    non_json_section = "others"
    non_json_data = json_data.get(non_json_section, None)
    if non_json_data:
        json_to_csv(json_data, non_json_section)
        metadata[non_json_section] = list(non_json_data.keys())

    return metadata

