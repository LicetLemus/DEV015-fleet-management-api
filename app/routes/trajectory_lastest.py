from flask import Blueprint
from app.controllers.trajectory_latest import get_trajectory_latest

bp_latest = Blueprint("latest", __name__)


@bp_latest.route("/trajectories/latest", methods=["GET"])
def handle_get_trajectory_latest():
    print("------------------------------- handle_get_trajectory_latest")
    return get_trajectory_latest()
