import json


def load_data_from_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def insert_data_if_empty(mongo, data):
    collection = mongo.db["cs-skins"]
    if collection.count_documents({}) == 0:
        collection.insert_many(data)
        print("Data inserted into 'cs-skins' collection.")
    else:
        print("'cs-skins' collection is not empty, skipping data insertion.")
