from flask import Blueprint
from app.controllers.taxi_location import get_location_taxi

bp_location = Blueprint("location", __name__)


bp_location.route('/taxi-locations', methods=['GET'])
def handle_get_location_taxi():
    return get_location_taxi()
