from flask import Blueprint, request
from app.controllers.user_controller import create_user, list_all_users, update_user, delete_user

bp_user = Blueprint("user", __name__)


@bp_user.route("/users", methods=["GET","POST"])
def create_or_list_users():
    if request.method == "POST":
        return create_user()
    if request.method == "GET":
        return list_all_users()
    

@bp_user.route("/users/<uid>", methods=["PATCH", "DELETE"])
def update_or_delete_user(uid): 
    if request.method == "PATCH":
        return update_user(uid)
    if request.method == "DELETE":
        return delete_user(uid)