import hmac
import hashlib

SERVER_SECRET = "BankServerSecret123"

def generate_key(response, j):

    message = (response + j)

    key = hmac.new(
        SERVER_SECRET.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

    return key