from flask import Blueprint
from app.controllers.create_user_controller import create_user

bp_create_user = Blueprint("user", __name__)


@bp_create_user.route("/users", methods=["POST"])
def handle_create_users():
    return create_user()