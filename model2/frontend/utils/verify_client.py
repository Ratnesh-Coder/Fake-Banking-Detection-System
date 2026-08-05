import requests

def verify_response(response, nonce):

    result = requests.post(
        "http://127.0.0.1:5000/verify",
        json={
            "response": response,
            "nonce": nonce
        }
    )
    
    return result.json()