from flask_jwt_extended import create_access_token
from flask import Blueprint, request, jsonify
from app.models.users import Users
from werkzeug.security import check_password_hash

bp_auth = Blueprint("auth", __name__)


@bp_auth.route("/auth", methods=["POST"])
def auth():

    data = request.get_json()

    email = data.get("email")
    password_data = data.get("password")

    try:
        # Check if email and password are provided
        if not email or not password_data:
            return jsonify({"error": "Missing email or password"}), 400

        # Search de user in the database
        user = Users.query.filter_by(email=email).first()

        # Verifica si el usuario existe y la contraseña es correcta
        if user and check_password_hash(user.password, password_data):
            access_token = create_access_token(identity=user.id)
            print(f"Password matched for user: {user.email}")
        else:
            print(f"Failed login attempt for user: {email}")
            return jsonify({"error": "Unauthorized access"}), 401


        # Devuelve el token de acceso

        return (
            jsonify(
                {
                    "access_token": access_token,
                    "user": {
                        "id": user.id,
                        "name": user.name,
                    },
                }
            ),
            200,
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500
