import os
import requests
import json

def send_authenticated_request(api_url, json_file_path, api_key):
    # Load parameters from JSON file
    with open(json_file_path, 'r') as file:
        params = json.load(file)

    # Set the token in the request headers
    headers = {
        'X-Api-Key': api_key,
        'Content-Type': 'application/json',
    }

    # Send POST request to the API with authentication headers
    response = requests.post(api_url, json=params, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Request successful. Response:")
        print(response.json())
        print(response.text)
    else:
        print(f"Request failed. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Replace these values with your connector's Management-API URL, JSON file path, and authentication token
    api_url = "https://connector-name.connector.mds.think-it.io/api/management/v2/transferprocesses"
    """
    Management API Endpoints:
    For asset creation: /api/management/v3/assets
    For requesting a transfer: /api/management/v2/transferprocesses
    """
    json_file_path = r"C:\Users\full-path\api__request_no_params.json"
    api_key = 'api-key provided by MDS support'

    send_authenticated_request(api_url, json_file_path, api_key)
