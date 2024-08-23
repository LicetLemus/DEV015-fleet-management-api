# blueprint: is a way to organize the routes of the application.
# jsonify: is a function that returns a response object with the application/json content type.

from flask import jsonify, Blueprint
from sqlalchemy import text
from src.database.db_sql import get_connection

bp_taxis = Blueprint("taxis", __name__) # create a blueprint for the taxis


@bp_taxis.route('/taxis', methods=['GET']) # create a route for the taxis
def get_taxis():
    
    connection = get_connection()
    
    if not connection:
        return jsonify({"error": "Error connecting to the database"})
    
    try:
        result = connection.execute(text("SELECT id, plate  FROM taxis"))
        table_taxis = []
            
        for row in result:
            table_taxis.append({"id": row[0], "plate": row[1]})

        return jsonify({"taxis": table_taxis})
        
    except Exception as e:
        return jsonify({"error": str(e)})
    
    finally:
        connection.close()
        print("Connection closed")