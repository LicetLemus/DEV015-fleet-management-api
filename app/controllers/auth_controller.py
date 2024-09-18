from flask import jsonify, request
from app.services.auth_services import authentic_user


def handle_login():
    data = request.get_json()
    email = data.get("email")
    password_data = data.get("password")

    # Check if email and password are provided
    if not email or not password_data:
        return jsonify({"error": "Missing email or password"}), 400

    try:
        response, status_code = authentic_user(email, password_data)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        