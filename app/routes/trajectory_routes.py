from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.trajectory_controller import get_trajectories

bp_location = Blueprint("trajectories", __name__)


@bp_location.route("/trajectories", methods=["GET"])
@jwt_required()
def handle_get_trajectories():
    """
    Fetches trajectory data based on `taxiId` and `date`.

    Returns:
    - JSON with trajectory data or error message.
    - Status code: 200, 400, 404, 500.
    """

    print("------------------------------- handle_get_trajectories")
    return get_trajectories()
