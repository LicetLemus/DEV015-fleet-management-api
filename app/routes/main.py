from flask import Blueprint
from flask_jwt_extended import jwt_required

bp_main = Blueprint("main", __name__)


@bp_main.route("/")
@jwt_required()
def handle_main():
    return "<h1>¡Hola, mundo!</h1>"
