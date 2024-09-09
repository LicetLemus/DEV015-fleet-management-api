from flask import request, jsonify
from app.services.create_user_service import insert_user


def create_user():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    if not name or not email or not password:
        return jsonify({"error": "Name, email, and password are required"}), 400

    try:
        user, status_code = insert_user(name, email, password)
        
        return jsonify(user), status_code
        
    except Exception as e:
        return jsonify({"Error": str(e)}), 500