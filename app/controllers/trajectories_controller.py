from flask import jsonify, request
from datetime import datetime
from app.services.trajectories_services import fetch_trajectories

def get_trajectories():
    """
    Gets all trajectories for a specific taxi on a date range in format JSON.

    Query Parameters:
    - taxi_id: ID of the taxi (string).
    - date: Date in format dd-mm-yyyy.

    Responses:
    - 200 OK: Returns a JSON list of trajectories.
    - 400 Bad Request: If taxi_id or date is missing, or if the date format is incorrect.
    - 404 Not Found: If no trajectories are found for the given taxi and date.
    - 500 Internal Server Error: In case of server error.

    Returns:
    - Flask Response: JSON with the result of the query or an error message.
    """
    
    print("------------------------------- get_trajectories") 
    taxi_id = request.args.get('taxi_id', type=str)
    date_str = request.args.get('date', type=str)
    
    # Check if exist taxi_id and date
    if not taxi_id or not date_str:
        return jsonify({"error": "taxi_id and date are required"}), 400
    
    date_initial_str, date_end_str = parse_date(date_str)

    try:
        # Fetch trajectories from the database using the given taxi_id and date range
        result_query = fetch_trajectories(taxi_id, date_initial_str, date_end_str)
        
        if 'error' in result_query:
            return jsonify(result_query), 404
        
        return jsonify({"trajectories": result_query}), 200
    
    except Exception as e:
        # Handle any exceptions that occur during the process
        return jsonify({"Error": str(e)}), 500
    

def parse_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%d-%m-%Y')
        date_initial = date_obj.replace(hour=0, minute=0, second=0, microsecond=0)
        date_end = date_obj.replace(hour=23, minute=59, second=59, microsecond=999999)
        return date_initial.strftime('%Y-%m-%d %H:%M:%S'), date_end.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return None, None