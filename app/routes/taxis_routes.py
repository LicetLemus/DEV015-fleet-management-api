from flask import Blueprint
from app.controllers.taxis_controller import get_taxis

bp_taxis = Blueprint("taxis", __name__)

@bp_taxis.route('/taxis', methods=['GET'])
def handle_get_taxis():
    return get_taxis()