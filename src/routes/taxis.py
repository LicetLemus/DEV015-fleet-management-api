# blueprint: is a way to organize the routes of the application.
# jsonify: is a function that returns a response object with the application/json content type.

from flask import jsonify, Blueprint, request
from sqlalchemy import text
from src.database.db_sql import get_session
from src.models.taxis import Taxis

bp_taxis = Blueprint("taxis", __name__) # create a blueprint for the taxis

# @bp_taxis.route('/taxis', defaults = {'plate': None, 'page':None, 'limit': None}, methods=['GET'])
# @bp_taxis.route('/taxis/<string:plate>', defaults = {'page':None,'limit': None}, methods=['GET'])
# @bp_taxis.route('/taxis/<string:plate>/<int:page>', defaults = {'limit': None}, methods=['GET'])
@bp_taxis.route('/taxis', methods=['GET']) # create a route for the taxis
def get_taxis():
    
    session = get_session()
    
    if not session:
        return jsonify({"error": "Error connecting to the database"})
    
    try:

        plate = request.args.get('plate', type = str)
        page = request.args.get('page', type = int, default = 1)
        limit = request.args.get('limit', type = int, default = 10)

        result_query = session.query(Taxis) # value initial
            
        if plate:
            result_query = result_query.filter(Taxis.plate == plate)
        
        elif page and limit:
            pass
        
        table_taxis = []
            
        for row in result_query:
            table_taxis.append({"id": row.id, "plate": row.plate})

        return jsonify({"taxis": table_taxis}), 200
        
    except Exception as e:
        return jsonify({"Error: An error occurred": str(e)})
    
    finally:
            session.close()
            print("Session closed")
            