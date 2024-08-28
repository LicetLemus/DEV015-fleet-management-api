from flask import jsonify, request
from app.services.taxis_services import fetch_taxis

def get_taxis():
    plate = request.args.get('plate', type=str, default=None)
    page = request.args.get('page', type=int, default=None)
    limit = request.args.get('limit', type=int, default=None)
    
    if page < 0 or limit < 0:
        return jsonify({"error": "Page number and limit must be greater than 0."}), 400

    try:
        taxis, status_code = fetch_taxis(plate, page, limit)
        
        if status_code == 404:
            return jsonify({"error": "No taxis found."}), 404
        
        return jsonify({"taxis": taxis}), 200
    
    except Exception as e:
        return jsonify({"Error": str(e)}), 500