# blueprint: is a way to organize the routes of the application.
# jsonify: is a function that returns a response object with the application/json content type.

from flask import jsonify
from sqlalchemy import text


def register_routes(app, engine):
    @app.route('/taxis', methods=['GET']) # create a route for the taxis
    def get_taxis():
        try:
            with engine.connect() as connection:
                result = connection.execute(text("SELECT id, plate  FROM taxis"))

                table_taxis = []
            
                for row in result:
                    table_taxis.append({"id": row[0], "plate": row[1]})

                return jsonify({"taxis": table_taxis})
        
        except Exception as e:
            return jsonify({"error": str(e)})
        
        
        
# @app.route('/taxis', methods=['GET']) # create a route for the taxis
# def get_taxis():
#     try:
#         with engine.connect() as connection:
#             result = connection.execute(text("SELECT id, plate  FROM taxis"))

#             table_taxis = []
        
#             for row in result:
#                 table_taxis.append({"id": row[0], "plate": row[1]})

#             connection.close()
#             return table_taxis
    
#     except Exception as e:
#         return jsonify({"error": str(e)}) 