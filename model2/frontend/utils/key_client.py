import requests

def get_key():

    response = requests.get(
        "http://127.0.0.1:5000/key"
    )

    return response.json()["key"]