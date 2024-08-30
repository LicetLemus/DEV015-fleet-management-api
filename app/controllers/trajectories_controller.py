from flask import jsonify, request
from datetime import datetime
from app.services.trajectories_services import fetch_trajectories

def get_trajectories():
    print("------------------------------- get_trajectories") 
    taxi_id = request.args.get('taxi_id', type=str)
    date = request.args.get('date', type=str)
    
    if not taxi_id or not date:
        return jsonify({"error": "taxi_id and date are required"}), 400

    # Validar el formato de la fecha
    try:
        # Intentar convertir la cadena de fecha a un objeto datetime
        date_obj = datetime.strptime(date, '%d-%m-%Y')
    except ValueError:
        # Si falla, el formato de la fecha es incorrecto
        return jsonify({"error": "Date format must be dd-mm-yyyy"}), 400
    
    # Ajustar la fecha inicial y final para todo el día
    date_initial = date_obj.replace(hour=0, minute=0, second=0, microsecond=0)
    date_end = date_obj.replace(hour=23, minute=59, second=59, microsecond=999999)
    
    # Convertir el objeto datetime a formato timestamp
    date_initial = date_initial.strftime('%Y-%m-%d %H:%M:%S')
    date_end = date_end.strftime('%Y-%m-%d %H:%M:%S')

    try:
        result_request = fetch_trajectories(taxi_id, date_initial, date_end)
        
        if 'error' in result_request:
            return jsonify(result_request), 404
        
        return jsonify({"trajectories": result_request}), 200
    
    except Exception as e:
        return jsonify({"Error": str(e)}), 500