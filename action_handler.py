
# This app takes an action name as an argument and sends a POST request to the DoAction endpoint
# of the Streamer.bot API to execute the action.
# For example, to run the action "MyAction", you would run the following command:
# python action_handler.py MyAction

import sys
import json
import requests


# Settings
# Usually no need to change these settings
HTTP_HOST = "127.0.0.1"
HTTP_PORT = "7474"
url = f"http://{HTTP_HOST}:{HTTP_PORT}/DoAction"

# Define the action name
ACTION_NAME = "".join(sys.argv[1:])  # Directly setting the action name

print(f"Attempting to run {ACTION_NAME}...")

# Preparing the data for the POST request
# If you have specific arguments to send, include them in the 'args' dictionary.
data = json.dumps({
    "action": {
        "name": ACTION_NAME
        # "id": "<guid>"  # Uncomment and provide the GUID if required
    },
    "args": {
        # "key": "value",  # Example argument, include if necessary
    }
})

# Sending the POST request
response = requests.post(url, data=data, headers={"Content-Type": "application/json"}, timeout=30)

# Checking if the request was successful
# Expecting a 204 No Content response for a successful action execution
if response.status_code == 204:
    print(f"Successfully ran {ACTION_NAME}")
else:
    print(f"Failed to run {ACTION_NAME}. Response code: {response.status_code}, Response body: {response.text}")
