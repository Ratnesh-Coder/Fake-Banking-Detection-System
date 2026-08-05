from flask import Blueprint, jsonify
from services.h2_service import get_h2

h2_bp = Blueprint("h2", __name__)

@h2_bp.route("/h2", methods=["GET"])
def send_h2():

    h2_code, j = get_h2()

    return jsonify({
        "h2": h2_code,
        "j": j
    })