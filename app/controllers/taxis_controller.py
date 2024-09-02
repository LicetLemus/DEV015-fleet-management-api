from flask import jsonify, request
from app.services.taxis_services import fetch_taxis

def get_taxis():
    """
    Get taxi information based on optional query parameters for filtering and pagination.

    Query Parameters:
    - plate_filter (str, optional): The plate number to filter taxis by. Default is None.
    - page_number (int, optional): The page number for pagination. Default is 1.
    - records_per_page (int, optional): The number of records per page. Default is 10.

    Returns:
    - JSON: A JSON object containing the list of taxis or an error message.
    """
    #get query params
    plate, page, limit = get_query_params()
    
    if page < 0 or limit < 0:
        return jsonify({"error": "Page number and limit must be greater than 0."}), 400

    try:
        taxis_data = fetch_taxis(plate, page, limit)
        print('resultado----------------', taxis_data)
        
        return jsonify(taxis_data), 200
 
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    

def get_query_params():
    """
    get query parameters from the request.

    Return:
    - the 'plate', 'page', and 'limit' parameters.
    """
    plate = request.args.get('plate', type=str, default=None)
    page = request.args.get('page', type=int, default=0)
    limit = request.args.get('limit', type=int, default=0)
    
    return plate, page, limit
    