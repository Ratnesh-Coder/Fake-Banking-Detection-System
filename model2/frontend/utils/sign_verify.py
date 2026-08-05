from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

with open(
    "keys/public.pem",
    "rb"
) as f:

    public_key = serialization.load_pem_public_key(
        f.read()
    )


def verify_signature(
    key,
    signature_hex
):

    try:

        signature = bytes.fromhex(
            signature_hex
        )

        public_key.verify(
            signature,
            key.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        return True

    except:

        return False