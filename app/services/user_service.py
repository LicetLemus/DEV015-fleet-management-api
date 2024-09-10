from flask import jsonify
from app.database.db_sql import get_session
from app.utils.validation_session import validation_session
from app.models.users import Users

# import uuid


def insert_user_to_db(name, email, password):

    session = get_session()
    validation_session(session)

    try:
        existing_user = session.query(Users).filter_by(email=email).first()
        if existing_user:
            return {"error": "The user already exists"}, 409

        new_user = Users(name=name, email=email, password=password)
        session.add(new_user)
        session.commit()

        response = {"id": new_user.id, "name": new_user.name, "email": new_user.email}

        return response, 201

    except Exception as e:
        return jsonify({"Error": str(e)}), 500

    finally:
        session.close()
        print("Session closed")


def fetch_users_from_db(page, limit):

    session = get_session()
    validation_session(session)

    try:
        query = session.query(Users)

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
        session.close()
        print("Session closed")


def update_user_in_db(uid, name, email, password):
    session = get_session()
    validation_session(session)

    try:
        user = session.query(Users).filter(Users.id == uid).first()

        if not user:
            return {"error": "User not found"}, 404

        if name:
            user.name = name
        if email or password:
            return {"error": "fields can not be updated"}, 400

        session.add(user)
        session.commit()

        response = {"id": user.id, "name": user.name, "email": user.email}

        return response, 200

    except Exception as e:
        return {"error": str(e)}, 500

    finally:
        session.close()
        print("Session closed")


def remove_user_from_db(uid):
    session = get_session()
    validation_session(session)

    try:
        user = session.query(Users).filter(Users.id == uid).first()

        if not user:
            return {"error": "User not found"}, 404

        session.delete(user)
        session.commit()
        
        response = {"id": user.id, "name": user.name, "email": user.email}

        return response, 200

    except Exception as e:
        return {"error": str(e)}, 500

    finally:
        session.close()
        print("Session closed")