import hashlib

def compute_i():

    with open("data/h1.py", "rb") as f:
        data = f.read()

    return hashlib.sha256(data).hexdigest()


def compute_j():

    with open("data/h2.py", "rb") as f:
        data = f.read()

    return hashlib.sha256(data).hexdigest()