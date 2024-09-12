from app.database.db_sql import db
from flask import jsonify
from app.models.taxis import Taxis


def fetch_taxis(plate, page, limit):
    """
    Retrieve a list of taxis with optional filtering and pagination.

    Args:
        plate (str): Optional filter to search taxis by license plate.
        page (int): Page number for pagination (must be greater than 0).
        limit (int): Number of records per page (must be greater than 0).

    Return:
        tuple: (list of taxis or error message, HTTP status code)
            - 200: OK
            - 404: Not Found (if no taxis are found)
            - 500: Internal Server Error (if an exception occurs)
    """

    try:
        # Initialize the query
        query = db.session.query(Taxis)

        if plate:
            query = query.filter(Taxis.plate.ilike(f"%{plate}%"))

        if page and limit:
            # calculate the number of results to skip
            offset = (page - 1) * limit
            # if pagination is applied
            query = query.offset(offset).limit(limit)

        # Execute the query and fetch results
        taxi_results = query.all()

        # Build the response
        if not taxi_results:
            return ({"error": "No taxis found."}), 404

        response = [{"id": taxi.id, "plate": taxi.plate} for taxi in taxi_results]

        return response, 200

    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    
    finally:
        db.session.close()
        print("Session closed")
