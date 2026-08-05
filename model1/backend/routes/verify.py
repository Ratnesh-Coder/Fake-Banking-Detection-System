from flask import Blueprint, request, jsonify
from services.hash_service import verify_hash
from config import ORIGINAL_HASH
import os

verify_bp = Blueprint('verify', __name__)

@verify_bp.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    client_hash = data.get("hash")

    if verify_hash(client_hash):

        with open("modules/h2.py", "r") as f:
            h2_code = f.read()

        with open("storage/h2_hash.txt", "r") as f:
            J = f.read().strip()

        return jsonify({
            "status": "VALID",
            "hash": ORIGINAL_HASH,
            "h2": h2_code,
            "j": J
        })
    else:
        return jsonify({"status": "INVALID"})