import requests
import os

def trigger_workflow():

    # Set the required information for the API request
    repository = "https://github.com/WoodyXP/Pyjulia"
    personal_token = os.getenv("GITHUB_TOKEN")
    workflow_file = "downstream.yml"

    # Construct the API endpoint URL
    api_url = f"https://api.github.com/repos/{repository}/actions/workflows/{workflow_file}/dispatches"

    # Set the request headers
    headers = {
        "Authorization": f"Bearer {personal_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Define the request payload
    payload = {
        "ref": "main",
        "inputs": {
            "param1": "value1",
            "param2": "value2"
        }
    }

    # Send the API request
    response = requests.post(api_url, headers=headers, json=payload)

    # Check the response status code
    if response.status_code == 204:
        print("Downstream workflow triggered successfully.")
    else:
        print("Failed to trigger downstream workflow.")

# Trigger the downstream workflow
trigger_workflow()
