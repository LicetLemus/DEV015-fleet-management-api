from flask import request, jsonify
from app.services.user_service import (
    insert_user_to_db,
    fetch_users_from_db,
    update_user_in_db,
)


def create_user():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"error": "Name, email, and password are required"}), 400

    try:
        user, status_code = insert_user_to_db(name, email, password)

        return jsonify(user), status_code

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


def list_user():
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


def process_user_update(uid):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400  # Manejo de caso sin datos

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
