import hashlib

def get_h2():

    with open("data/h2.py", "r") as f:
        h2_code = f.read()

    j = hashlib.sha256(
        h2_code.encode()
    ).hexdigest()

    return h2_code, j