import requests
import json

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP error occurred: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection error occurred: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout error occurred: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

def save_data(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"An error occurred when writing to file: {e}")

url = 'https://bymykel.github.io/CSGO-API/api/en/skins_not_grouped.json'

data = fetch_data(url)

if data is not None:
    save_data(data, 'data.json')
    print("Data successfully saved to 'data.json'.")
else:
    print("No data to save.")
