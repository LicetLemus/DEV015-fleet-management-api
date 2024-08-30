from flask import jsonify, request
from datetime import datetime
from app.services.trajectories_services import fetch_trajectories

def get_trajectories():
    print("------------------------------- get_trajectories") 
    taxi_id = request.args.get('taxi_id', type=str)
    date = request.args.get('date', type=str)
    
    if not taxi_id or not date:
        return jsonify({"error": "taxiId and date are required"}), 400

    # Convertir la cadena de fecha al formato deseado
    try:
        date = datetime.strptime(date, '%d-%m-%Y')
    except ValueError:
        return jsonify({"error": "Date format must be dd-mm-yyyy"}), 400

    try:
        result_request = fetch_trajectories(taxi_id, date)
        
        return jsonify({"trajectories": result_request}), 200
    
    except Exception as e:
        return jsonify({"Error": str(e)}), 500