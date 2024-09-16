from app.models.users import Users
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
import datetime


def authentic_user(email, password_data):

    try:
        # Filter in database for the user
        user = Users.query.filter_by(email=email).first()

        if not user:
            return {'error': 'User not found'}, 404

        # Check if password is valid
        if not check_password_hash(user.password, password_data):
            return {"error": "Unauthorized access"}, 401
        
        ## Generate access token
        access_token = create_access_token(
            identity=user.id,
            expires_delta=datetime.timedelta(seconds=30)  # Token expires in 1 hour
            )

        return (
            {
                "access_token": access_token,
                "user": {
                    "id": user.id,
                    "name": user.name,
                },
            },
            200,
        )

    except Exception as e:
        return {"error": str(e)}, 500
