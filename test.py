import requests
import json

BASE = "http://127.0.0.1:5000/"

data = {"likes": 10}  # Data to be sent as JSON

response = requests.patch(BASE + "video/1", json=data)  # Use PATCH method for update

if response.status_code == 200:
    try:
        data = response.json()
        print(data)
    except ValueError:
        print("Response is not valid JSON.")
else:
    print("Request failed with status code:", response.status_code)
