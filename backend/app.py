from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def extract_data():
    # Load JSON data from a file
    with open('data.json', 'r') as file:
        data = json.load(file)

    results = {}
    if isinstance(data, list):
        for item in data:
            if 'id' in item:
                results[item['id']] = item
                break  # Only process the first item with an 'id'
    elif isinstance(data, dict) and 'id' in data:
        results[data['id']] = data

    return results

@app.route('/api/data', methods=['GET'])
def get_data():
    # Extract data from the JSON file
    extracted_data = extract_data()
    # Return the extracted data as a JSON response wrapped in a 'message' key
    return jsonify(message=extracted_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)
