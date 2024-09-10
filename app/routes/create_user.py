from flask import Blueprint, request
from app.controllers.create_user_controller import create_user, list_user

bp_create_user = Blueprint("user", __name__)


@bp_create_user.route("/users", methods=["GET","POST"])
def handle_create_user():
    if request.method == "POST":
        return create_user()
    if request.method == "GET":
        return list_user()