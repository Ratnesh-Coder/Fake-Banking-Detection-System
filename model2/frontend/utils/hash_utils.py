import hashlib

def compute_response(h1_path, nonce):

    with open(h1_path, "rb") as f:
        h1_data = f.read()

    response = hashlib.sha256(
        h1_data + nonce.encode()
    ).hexdigest()

    return response