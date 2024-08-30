from flask import jsonify, request
from datetime import datetime
from app.services.trajectories_services import fetch_trajectories

def get_trajectories():
    """
    Gets all trajectories for a specific taxi within a date range.

    Query Parameters:
    - taxi_id (str): ID of the taxi.
    - date (str): Date in 'dd-mm-yyyy' format.

    Returns:
    - Flask Response: JSON with the list of trajectories or an error message.
    """
    print("------------------------------- get_trajectories") 
    
    taxi_id, date_str = get_query_params_trajectories()
    
    validation_result = validation_query_params_trajectories(taxi_id, date_str)
    if validation_result:
        return validation_result
    
    date_initial_str, date_end_str = parse_date(date_str)
    if not date_initial_str or not date_end_str:
        return jsonify({"error": "Date must be in 'dd-mm-yyyy' format."}), 400

    try:
        result_query = fetch_trajectories(taxi_id, date_initial_str, date_end_str)
        
        if 'error' in result_query:
            return jsonify(result_query), 404
        
        return jsonify({"trajectories": result_query}), 200
    
    except Exception as e:
        # Handle any exceptions that occur during the process
        return jsonify({"Error": str(e)}), 500


def get_query_params_trajectories():
    """
    Retrieve query parameters for taxi ID and date from the request.

    Returns:
    - (taxi_id, date_str)
    """
    taxi_id = request.args.get('taxi_id', type=str)
    date_str = request.args.get('date', type=str)
    
    return taxi_id, date_str


def validation_query_params_trajectories(taxi_id, date_str):
    """
    Validate taxi_id and date_str parameters.

    Args:
    - taxi_id (str): ID of the taxi.
    - date_str (str): Date in 'dd-mm-yyyy' format.

    Returns:
    - Flask Response: JSON with an error message and a 400 status code if validation fails, otherwise None.
    """
    if not taxi_id or not date_str:
        return jsonify({"error": "taxi_id and date are required"}), 400


def parse_date(date_str):
    """ 
    Parse the date string and return the start and end of the day in 'YYYY-MM-DD HH:MM:SS' format.

    Args:
    - date_str (str): Date in 'dd-mm-yyyy' format.

    Return:
    - (start_of_day, end_of_day) in 'YYYY-MM-DD HH:MM:SS' format.
    """

    try:
        date_obj = datetime.strptime(date_str, '%d-%m-%Y')
        date_initial = date_obj.replace(hour=0, minute=0, second=0, microsecond=0)
        date_end = date_obj.replace(hour=23, minute=59, second=59, microsecond=999999)
        return date_initial.strftime('%Y-%m-%d %H:%M:%S'), date_end.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return None, None
    