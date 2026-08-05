import requests

def get_nonce():
    response = requests.get(
        "http://127.0.0.1:5000/nonce"
    )

    return response.json()["nonce"]