from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.trajectory_latest_controller import get_trajectory_latest

bp_latest = Blueprint("latest", __name__)


@bp_latest.route("/trajectories/latest", methods=["GET"])
@jwt_required()
def handle_get_trajectory_latest():
    """
    Handles GET requests to the /trajectories/latest endpoint.

    Delegates the request to `get_trajectory_latest` to retrieve the latest trajectory data.

    Return:
    - JSON: The latest trajectory data or an error message.
    - Status Code: 200 if successful, 500 if an error occurs.
    """

    return get_trajectory_latest()
