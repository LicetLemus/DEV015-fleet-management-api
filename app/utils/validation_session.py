from flask import jsonify

def validation_session(session):
    if not session:
        return jsonify({"error": "Error connecting to the database"}), 500
    print('Connected to database')