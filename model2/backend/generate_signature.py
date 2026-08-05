from services.key_service import generate_key
from services.hash_service import (compute_i, compute_j)

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

I = compute_i()
J = compute_j()

with open("keys/private.pem", "rb") as f:

    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

key = generate_key(I, J)

signature = private_key.sign(
    key.encode(),
    padding.PKCS1v15(),
    hashes.SHA256()
)

with open("../frontend/signature.txt", "w") as f:

    f.write(
        signature.hex()
    )

print("Signature generated.")