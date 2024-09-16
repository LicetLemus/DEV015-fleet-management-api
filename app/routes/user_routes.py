from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.controllers.user_controller import create_user, list_all_users, update_user, delete_user

bp_user = Blueprint("user", __name__)


@bp_user.route("/users", methods=["POST"])
def create_user_route():
    return create_user()

@bp_user.route("/users", methods=["GET"])
@jwt_required()
def list_all_users_route():
    return list_all_users()
    

@bp_user.route("/users/<uid>", methods=["PATCH", "DELETE"])
@jwt_required()
def update_or_delete_user(uid): 
    if request.method == "PATCH":
        return update_user(uid)
    if request.method == "DELETE":
        return delete_user(uid)