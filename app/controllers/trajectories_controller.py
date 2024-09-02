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
    
    if not taxi_id or not date_str:
        return jsonify({"error": "taxi_id and date are required"}), 400
    
    date_initial_str, date_end_str = parse_date(date_str)
    if not date_initial_str or not date_end_str:
        return jsonify({"error": "Date must be in 'dd-mm-yyyy' format."}), 400

    try:
        trajectories_data, status_code = fetch_trajectories(taxi_id, date_initial_str, date_end_str)
        print('trajectories_result-------', trajectories_data, status_code)
        
        # Return the data or error message
        return jsonify(trajectories_data), status_code
    
    except Exception as e:
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
    