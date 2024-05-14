import os
import requests
import json


def get_authentication_token(script_path):
    # Run the shell script and capture its output
    result = os.popen(script_path).read()

    # Parse the JSON output
    try:
        json_result = json.loads(result)
        authentication_token = json_result['access_token']
        return authentication_token
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from the script output: {e}")
        return None


def send_authenticated_request(api_url, json_file_path, token):
    # Load parameters from JSON file
    with open(json_file_path, 'r') as file:
        params = json.load(file)

    # Set the token in the request headers
    headers = {
        'Authorization': f'Bearer {token}',
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
    # Replace these values with your API URL, JSON file path, and authentication token
    api_url = "[please set your CaaS base url] + Management API Endpoint"
    """
    Management API Endpoints:
    For asset creation: /api/management/v3/assets
    For requesting a transfer: /api/management/v2/transferprocesses
    """
    json_file_path = "[please set the path to the json config file]"
    script_path = "[please set the path to the api_authent_curl script]"

    authentication_token = get_authentication_token(script_path)
    send_authenticated_request(api_url, json_file_path, authentication_token)
