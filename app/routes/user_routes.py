from flask import Blueprint, request
from app.controllers.user_controller import create_user, list_user, process_user_update, delete_user

bp_user = Blueprint("user", __name__)


@bp_user.route("/users", methods=["GET","POST"])
def handle_create_list_user():
    if request.method == "POST":
        return create_user()
    if request.method == "GET":
        return list_user()
    

@bp_user.route("/users/<uid>", methods=["PATCH", "DELETE"])
def handle_update_user(uid): 
    if request.method == "PATCH":
        return process_user_update(uid)
    if request.method == "DELETE":
        return delete_user(uid)