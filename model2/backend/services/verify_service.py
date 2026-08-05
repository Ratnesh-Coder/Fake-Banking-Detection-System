import hashlib

def verify_response(response, nonce):

    with open("../frontend/modules/h1.py", "rb") as f:
        h1_data = f.read()

    expected = hashlib.sha256(
        h1_data + nonce.encode()
    ).hexdigest()

    return {
        "valid": expected == response,
        "expected_response": expected
    }