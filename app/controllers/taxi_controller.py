from flask import jsonify, request
from app.services.taxi_service import fetch_taxis


def get_taxis():
    """
    Fetch taxi information with optional filtering and pagination.

    Query Parameters:
        - plate (str, optional): Filter taxis by plate number.
        - page (int, optional): Page number for pagination (default is 1).
        - limit (int, optional): Records per page (default is 10).

    Return:
        - JSON response with taxi data or error message.
        - Status code: 200 (OK), 400 (Bad Request), 404 (Not Found), 500 (Internal Server Error).
    """

    plate, page, limit = get_query_parameters()

    if page < 0 or limit < 0:
        return jsonify({"error": "Page number and limit must be greater than 0."}), 400

    try:
        # Fetch taxi data from service
        taxis_data, status_code = fetch_taxis(plate, page, limit)

        # Return the data and status
        return jsonify(taxis_data), status_code

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


def get_query_parameters():
    """
    Get query parameters for taxi filtering and pagination.

    Returns:
        - plate (str or None): Plate number for filtering.
        - page (int): Page number (default is 1).
        - limit (int): Number of records per page (default is 10).
    """
    plate = request.args.get("plate", type=str, default=None)
    page = request.args.get("page", type=int, default=1)
    limit = request.args.get("limit", type=int, default=10)

    return plate, page, limit
