from flask import jsonify
from app.database.db_sql import db
from app.models.users import Users
from werkzeug.security import generate_password_hash


def create_user_in_db(name, email, password):

    try:
        existing_user = db.session.query(Users).filter_by(email=email).first()
        if existing_user:
            return {"error": "The user already exists"}, 409

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256') 
        new_user = Users(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        response = {"id": new_user.id, "name": new_user.name, "email": new_user.email}

        return response, 201

    except Exception as e:
        return jsonify({"Error": str(e)}), 500

    finally:
        db.session.close()
        print("Session closed")


def fetch_users_from_db(page, limit):

    try:
        query = db.session.query(Users)

        if page and limit:
            offset = (page - 1) * limit
            query = query.offset(offset).limit(limit)

        print(f"Limit applied-------------: {limit}")

        user_result = query.all()

        print(f"Number of users returned-------------------: {len(user_result)}")

        if not user_result:
            return {"error": "No user found"}, 404

        response = [
            {"id": user.id, "name": user.name, "email": user.email}
            for user in user_result
        ]
        return response, 200

    except Exception as e:
        return {"error": str(e)}, 500

    finally:
        db.session.close()
        print("Session closed")


def update_user_in_db(uid, name, email, password):

    try:
        user = db.session.query(Users).filter(Users.id == uid).first()

        if not user:
            return {"error": "User not found"}, 404

        if name:
            user.name = name
        if email or password:
            return {"error": "fields can not be updated"}, 400

        db.session.add(user)
        db.session.commit()

        response = {"id": user.id, "name": user.name, "email": user.email}

        return response, 200

    except Exception as e:
        return {"error": str(e)}, 500

    finally:
        db.session.close()
        print("Session closed")


def remove_user_from_db(uid):

    try:
        user = db.session.query(Users).filter(Users.id == uid).first()

        if not user:
            return {"error": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        
        response = {"id": user.id, "name": user.name, "email": user.email}

        return response, 200

    except Exception as e:
        return {"error": str(e)}, 500

    finally:
        db.session.close()
        print("Session closed")