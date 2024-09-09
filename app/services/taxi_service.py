from app.database.db_sql import get_session
from flask import jsonify
from app.utils.validation_session import validation_session
from app.models.taxis import Taxis


def fetch_taxis(plate, page, limit):
    """
    Get a list of taxis from the database, with optional filtering and pagination.

    Args:
        plate (str, optional): Filter to return only taxis with the specified license plate.
        page (int, optional): Page number for pagination. Must be greater than 0.
        limit (int, optional): Number of records per page for pagination. Must be greater than 0.

    Return:
        JSON: A list of taxis or an error message if an error occurs.
    """
    session = get_session()
    validation_session(session)

    try:
        # Initialize the query
        query = session.query(Taxis)

        if plate:
            query = query.filter(Taxis.plate.ilike(f"%{plate}%"))

        if page and limit:
            # Calcula el número de resultados a omitir
            offset = (page - 1) * limit
            # Si se aplica paginación
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
        session.close()
        print("Session closed")
