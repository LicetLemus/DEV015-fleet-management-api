from flask import jsonify, request
from app.services.taxis_services import fetch_taxis

def get_taxis():
    """
    Get taxi information based on optional query parameters.

    Query Parameters:
    - plate (str, optional): The plate number of the taxi to filter by. Default is None.
    - page (int, optional): The page number for pagination. Default is 0.
    - limit (int, optional): The number of records per page. Default is 0.

    Returns:
    - JSON: A JSON object containing the list of taxis and a 200 status code if successful.
    - JSON: An error message and a 400 status code if the page number or limit is negative.
    - JSON: An error message and a 500 status code if an exception occurs.
    """
    
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