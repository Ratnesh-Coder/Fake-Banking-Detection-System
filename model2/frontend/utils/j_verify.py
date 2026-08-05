import hashlib

def verify_j(h2_code, j):

    j_prime = hashlib.sha256(
        h2_code.encode()
    ).hexdigest()

    return j == j_prime, j_prime