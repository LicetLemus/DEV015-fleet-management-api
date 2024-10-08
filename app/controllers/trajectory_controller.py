from flask import jsonify, request
from datetime import datetime
from app.services.trajectory_service import fetch_trajectories


def get_trajectories():
    """
    Get trajectories for a specific taxi within a date range.

    Query Parameters:
        - taxiId (str): Taxi ID (required).
        - date (str): Date in 'dd-mm-yyyy' format (required).

    Returns:
        - JSON list of trajectories or an error message.
        - Status codes: 200 (OK), 400 (Bad Request), 404 (Not Found), 500 (Internal Server Error).
    """

    taxi_id, date_str = get_query_params_trajectories()

    if not taxi_id or not date_str:
        return jsonify({"error": "taxi_id and date are required"}), 400

    date_initial_str, date_end_str = parse_date(date_str)
    if not date_initial_str or not date_end_str:
        return jsonify({"error": "Date must be in 'dd-mm-yyyy' format."}), 400

    try:
        trajectories_data, status_code = fetch_trajectories(
            taxi_id, date_initial_str, date_end_str
        )
        print("trajectories_result-------", trajectories_data, status_code)

        # Return the data or error message
        return jsonify(trajectories_data), status_code

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


def get_query_params_trajectories():
    """
    Extracts query parameters for taxi ID and date.

    Return:
        - taxi_id (str): Taxi ID.
        - date_str (str): Date in 'dd-mm-yyyy' format.
    """
    taxi_id = request.args.get("taxiId", type=str)
    date_str = request.args.get("date", type=str)

    return taxi_id, date_str


def parse_date(date_str):
    """
    Converts a date string from 'dd-mm-yyyy' to start and end of the day in 'YYYY-MM-DD HH:MM:SS'.

    Args:
        - date_str (str): Date in 'dd-mm-yyyy' format.

    Returns:
        - (str, str): Start and end of the day in 'YYYY-MM-DD HH:MM:SS' format, or (None, None) if invalid.
    """

    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        date_initial = date_obj.replace(hour=0, minute=0, second=0, microsecond=0)
        date_end = date_obj.replace(hour=23, minute=59, second=59, microsecond=999999)
        return date_initial.strftime("%Y-%m-%d %H:%M:%S"), date_end.strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        return None, None
