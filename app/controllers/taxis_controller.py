from flask import jsonify, request
from app.services.taxis_services import fetch_taxis

def get_taxis():
    """
    Get taxi information based on optional query parameters.

    Query Parameters:
    - plate (str, optional): The plate number of the taxi to filter by. Default is None.
    - page (int, optional): The page number for pagination. Default is 0.
    - limit (int, optional): The number of records per page. Default is 0.

    Return:
    - JSON: A JSON object containing the list of taxis or An error message http
    """
    #get query params
    plate, page, limit = get_query_params()
    validation_result = validation_page_limit(page, limit)
    if validation_result:
        return validation_result

    try:
        result_request = fetch_taxis(plate, page, limit)
        
        return jsonify({"taxis": result_request}), 200
    
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

def validation_page_limit(page, limit):
    """
    Validate the page number and limit parameters.
    
    Args:
    - page (int): Page number.
    - limit (int): Number of records per page.

    Return:
    - JSON: An error message and a 400 status code if validation fails, otherwise None.
    """
    
    if page < 0 or limit < 0:
        return jsonify({"error": "Page number and limit must be greater than 0."}), 400