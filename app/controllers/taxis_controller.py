from flask import jsonify, request
from app.services.taxis_services import fetch_taxis

def get_taxis():
    """
    Get taxi information based on optional query parameters for filtering and pagination.

    Query Parameters:
    - plate (str, optional): The plate number to filter taxis by. Default is None.
    - page (int, optional): The page number for pagination. Default is 1.
    - limit (int, optional): The number of records per page. Default is 10.

    Returns:
    - JSON: A JSON object containing the list of taxis or an error message.
    """
    #get query params
    plate, page, limit = get_query_parameters()
    
    if page < 0 or limit < 0:
        return jsonify({"error": "Page number and limit must be greater than 0."}), 400

    try:
        # Fetch taxi data from service
        taxis_data, status_code = fetch_taxis(plate, page, limit)
        print('taxis_result-------', taxis_data, status_code)
        
        # Return the data or error message
        return jsonify(taxis_data), status_code

    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    

def get_query_parameters():
    """
    get query parameters from the request.

    Return:
    - the 'plate', 'page', and 'limit' parameters.
    """
    plate = request.args.get('plate', type=str, default=None)
    page = request.args.get('page', type=int, default=0)
    limit = request.args.get('limit', type=int, default=0)
    
    return plate, page, limit
    