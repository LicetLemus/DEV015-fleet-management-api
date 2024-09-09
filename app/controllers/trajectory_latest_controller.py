from flask import jsonify
from app.services.trajectory_latest_service import fetch_trajectory_latest


def get_trajectory_latest():
    """
    Get the latest trajectory data for all taxis.

    Returns:
        - JSON response with the latest trajectory data or an error message.
        - Status codes: 200 (OK), 500 (Internal Server Error).
    """

    try:
        latest_trajectory_data, status_code = fetch_trajectory_latest()
        return jsonify(latest_trajectory_data), status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500
