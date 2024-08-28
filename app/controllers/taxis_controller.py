from flask import jsonify, request
from app.services.taxis_services import fetch_taxis

def get_taxis():
    plate = request.args.get('plate', type=str, default=None)
    page = request.args.get('page', type=int, default=0)
    limit = request.args.get('limit', type=int, default=0)
    
    if page < 0 or limit < 0:
        return jsonify({"error": "Page number and limit must be greater than 0."}), 400

    try:
        result_request = fetch_taxis(plate, page, limit)
        
        return jsonify({"taxis": result_request}), 200
    
    except Exception as e:
        return jsonify({"Error": str(e)}), 500