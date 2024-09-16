from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.controllers.taxi_controller import get_taxis

bp_taxis = Blueprint("taxis", __name__)


@bp_taxis.route("/taxis", methods=["GET"])
@jwt_required()
def handle_get_taxis():
    """
    Handles GET requests to the /taxis endpoint.

    Calls `get_taxis` to retrieve and return taxi data based on optional query parameters.

    Returns:
        - JSON: Taxi data or an error message.
        - Status Code: 200 for success, 400 for bad request, or 500 for internal error.
    """
    return get_taxis()
