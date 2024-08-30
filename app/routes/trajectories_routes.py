from flask import Blueprint
from app.controllers.trajectories_controller import get_trajectories

bp_location = Blueprint("trajectories", __name__)


@bp_location.route('/trajectories', methods=['GET'])
def handle_get_trajectories():
    """
    Handle GET requests to the '/trajectories' endpoint.

    Query Parameters:
    Returns:
    - JSON response with the trajectories data if successful.
    - JSON response with an error message and HTTP 

    Example:
    GET /trajectories?taxi_id=123&date=31-12-2023

    Returns:
    - 200 OK with a JSON object containing the trajectories if the request is successful.
    - 400 Bad Request if required parameters are missing or the date format is incorrect.
    - 404 Not found if the trajectory list is not found
    - 500 Internal Server Error if an exception occurs during processing.
    """
    
    print("------------------------------- handle_get_trajectories")
    return get_trajectories()
