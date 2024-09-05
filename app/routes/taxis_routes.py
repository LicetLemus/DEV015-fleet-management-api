from flask import Blueprint
from app.controllers.taxis_controller import get_taxis

bp_taxis = Blueprint("taxis", __name__)


@bp_taxis.route("/taxis", methods=["GET"])
def handle_get_taxis():
    """
    Handles GET requests to the /taxis endpoint.

    This endpoint get a list of taxis based on optional query parameters:
    - `plate` (str): Filter taxis by their license plate.
    - `page` (int): The page number for pagination.
    - `limit` (int): The number of records per page for pagination.

    Returns:
    - JSON response containing a list of taxis or an error message.
    """

    return get_taxis()
