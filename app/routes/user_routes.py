from flask import Blueprint, request
from app.controllers.user_controller import create_user, list_user, process_user_update

bp_user = Blueprint("user", __name__)


@bp_user.route("/users", methods=["GET","POST"])
def handle_create_list_user():
    if request.method == "POST":
        return create_user()
    if request.method == "GET":
        return list_user()
    

@bp_user.route("/users/<uid>", methods=["PATCH"])
def handle_update_user(uid): 
    return process_user_update(uid)