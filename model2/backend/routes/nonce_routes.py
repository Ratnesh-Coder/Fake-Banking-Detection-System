from flask import Blueprint, jsonify
from services.nonce_service import generate_nonce

print("Nonce route loaded")

nonce_bp = Blueprint("nonce", __name__)

@nonce_bp.route("/nonce", methods=["GET"])
def get_nonce():
    nonce = generate_nonce()

    return jsonify({
        "nonce": nonce
    })