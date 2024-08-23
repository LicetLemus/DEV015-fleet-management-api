# from flask import Flask, jsonify
# from sqlalchemy import create_engine, text


# app = Flask(__name__)


# @app.route('/taxis', methods=['GET']) 
# def get_taxis():
#     try:

#         connection = engine.connect()
#         result = connection.execute(text("SELECT id, plate  FROM taxis"))

#         table_taxis = []
        
#         for row in result:
#             table_taxis.append({"id": row[0], "plate": row[1]})

#         # Devolver los resultados en formato JSON
#         return table_taxis
    
    
#     except Exception as e:
#         return jsonify({"error": str(e)})   
        

# if __name__ == '__main__':
#     app.run() # run the application