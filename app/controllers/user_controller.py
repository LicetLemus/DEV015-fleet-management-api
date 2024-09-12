from flask import request, jsonify
from app.services.user_service import (
    create_user_in_db,
    fetch_users_from_db,
    update_user_in_db,
    remove_user_from_db
)


def create_user():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"error": "Name, email, and password are required"}), 400

    try:
        user, status_code = create_user_in_db(name, email, password)

        return jsonify(user), status_code

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


def list_all_users():
    page_str = request.args.get("page", default=1)
    limit_str = request.args.get("limit", default=10)

    try:
        page = int(page_str)
        limit = int(limit_str)

    except ValueError:
        return jsonify({"error": "Page and limit must be integers."}), 400

    if page < 1 or limit < 1:
        return jsonify({"error": "Page number and limit must be greater than 0."}), 400

    try:
        user_data, status_code = fetch_users_from_db(page, limit)
        return jsonify(user_data), status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def update_user(uid):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400 

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if uid:
        try:
            data_user, status_code = update_user_in_db(uid, name, email, password)
            return jsonify(data_user), status_code

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    else:
        return jsonify({"error": "uid is required"}), 400


def delete_user(uid):

    if uid:
        try:
            response, status_code = remove_user_from_db(uid)
            return jsonify(response), status_code

        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "uid is required"}), 400