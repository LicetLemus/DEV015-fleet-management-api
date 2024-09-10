from flask import request, jsonify
from app.services.create_user_service import insert_user, get_user


def create_user():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"error": "Name, email, and password are required"}), 400

    try:
        user, status_code = insert_user(name, email, password)

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
        user_data, status_code = get_user(page, limit)
        return jsonify(user_data), status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500
