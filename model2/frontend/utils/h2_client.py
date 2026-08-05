import requests

def get_h2():

    response = requests.get(
        "http://127.0.0.1:5000/h2"
    )

    return response.json()