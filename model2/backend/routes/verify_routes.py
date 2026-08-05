from flask import Blueprint, request, jsonify
from services.verify_service import verify_response

verify_bp = Blueprint("verify", __name__)

@verify_bp.route("/verify", methods=["POST"])
def verify():

    data = request.get_json()

    result = verify_response(
        data["response"],
        data["nonce"]
    )

    return jsonify(result)