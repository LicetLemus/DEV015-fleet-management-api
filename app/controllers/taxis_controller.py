from flask import jsonify, request
from app.services.taxis_services import fetch_taxis

def get_taxis():
    plate = request.args.get('plate', type=str, default=None)
    page = request.args.get('page', type=int, default=None)
    limit = request.args.get('limit', type=int, default=None)

    try:
        taxis = fetch_taxis(plate, page, limit)
        return jsonify({"taxis": taxis}), 200
    
    except Exception as e:
        return jsonify({"Error": str(e)}), 500