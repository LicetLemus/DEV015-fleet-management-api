from flask import Blueprint
from app.controllers.trajectories_controller import get_trajectories

bp_location = Blueprint("trajectories", __name__)


@bp_location.route('/trajectories', methods=['GET'])
def handle_get_trajectories():
    print("------------------------------- handle_get_trajectories")
    return get_trajectories()
