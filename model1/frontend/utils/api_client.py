import requests

def verify_apk(hash_value):
    url = "http://127.0.0.1:5000/verify"
    response = requests.post(url, json={"hash": hash_value})
    return response.json()