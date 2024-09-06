from flask import jsonify
from app.services.trajectory_latest_service import fetch_trajectory_latest


def get_trajectory_latest():

    try:
        latest_trajectory_data, status_code = fetch_trajectory_latest()
        return jsonify(latest_trajectory_data), status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500
