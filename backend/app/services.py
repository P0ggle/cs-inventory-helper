import json


def extract_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    results = {}
    if isinstance(data, list):
        for item in data:
            if "id" in item:
                results[item["id"]] = item
                break  # Only process the first item with an 'id'
    elif isinstance(data, dict) and "id" in data:
        results[data["id"]] = data
    return results
