# blueprint: is a way to organize the routes of the application.
# jsonify: is a function that returns a response object with the application/json content type.

from flask import jsonify, Blueprint
from sqlalchemy import text
from src.database.db_sql import get_session
from src.models.taxis import Taxis

bp_taxis = Blueprint("taxis", __name__) # create a blueprint for the taxis

@bp_taxis.route('/taxis', defaults = {'plate': None, 'page':None, 'limit': None}, methods=['GET'])
@bp_taxis.route('/taxis/<string:plate>', defaults = {'page':None,'limit': None}, methods=['GET'])
@bp_taxis.route('/taxis/<string:plate>/<int:page>', defaults = {'limit': None}, methods=['GET'])
@bp_taxis.route('/taxis/<string:plate>/<int:page>/<int:limit>', methods=['GET']) # create a route for the taxis
def get_taxis(plate, page, limit):
    
    session = get_session()
    
    if not session:
        return jsonify({"error": "Error connecting to the database"})
    
    if plate == None and page == None and limit == None:
        try:
            result = session.query(Taxis).all()
            print(result)
            table_taxis = []
            
            for row in result:
                table_taxis.append({"id": row.id, "plate": row.plate})

            return jsonify({"taxis": table_taxis})
        
        except Exception as e:
            return jsonify({"error": str(e)})
    
        finally:
            session.close()
            print("Session closed")