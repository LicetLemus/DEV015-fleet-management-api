from flask import jsonify
from app.database.db_sql import get_session
from app.utils.validation_session import validation_session
from app.models.users import Users
# import uuid

def insert_user(name, email, password):
    
    session = get_session()
    validation_session(session)
    
    try:
        existing_user = session.query(Users).filter_by(email=email).first()
        if existing_user:
            return {"error": "The user already exists"}, 409
        
        new_user = Users(name=name, email=email, password=password)
        session.add(new_user)
        session.commit()
        
        response = {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }
        
        return response, 201
    
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

    finally:
        session.close()
        print("Session closed")