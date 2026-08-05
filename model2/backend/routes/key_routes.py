from flask import Blueprint, jsonify
from services.hash_service import (compute_i, compute_j)
from services.key_service import (generate_key)

key_bp = Blueprint("key", __name__)

@key_bp.route(
    "/key",
    methods=["GET"]
)
def get_key():
    i = compute_i()
    j = compute_j()
    key = generate_key(i, j)

    return jsonify({
        "key": key
    })