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
        result_query = session.query(Taxis)
        result_query = get_query_with_params(result_query, plate, page, limit)

        table_taxis = []

        for row in result_query:
            table_taxis.append({"id": row.id, "plate": row.plate})
        
        if not table_taxis:
            return {"error": "No taxis found."}, 404
            
        return table_taxis
        
    except Exception as e:
        return jsonify({"Error": str(e)})
        
    finally:
        session.close()
        print("Session closed")


def get_query_with_params(result_query, plate, page, limit):
    """
    Apply optional filtering and pagination to the query.

    Args:
        result_query (Query): SQLAlchemy query object to be modified.
        plate (str, optional): Filter to return only records with the specified plate.
        page (int, optional): Page number for pagination. Must be greater than 0.
        limit (int, optional): Number of records per page for pagination. Must be greater than 0.

    Return:
        Query: Modified SQLAlchemy query object with applied filters and pagination.
    """
    if plate:
            return result_query.filter(Taxis.plate == plate)

    if page and limit:
    # Calcula el número de resultados a omitir
        offset = (page - 1) * limit 
        # Si se aplica paginación
        return result_query.offset(offset).limit(limit)
    return result_query
    