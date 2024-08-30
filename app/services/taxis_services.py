from app.database.db_sql import get_session
from flask import jsonify
from app.models.taxis import Taxis

def fetch_taxis(plate, page, limit):
    """
    Get a list of taxis from the database, with optional filtering and pagination.

    Args:
        plate (str): Optional filter to return only taxis with the specified license plate.
        page (int): Page number for pagination. Must be greater than 0.
        limit (int): Number of records per page for pagination. Must be greater than 0.

    Returns:
        list or dict: A list of dictionaries representing taxis, or a dictionary with an error message if no taxis are found or if an error occurs.
        - Each dictionary in the list contains:
            - "id" (int): The ID of the taxi.
            - "plate" (str): The license plate of the taxi.
        - In case of an error, returns a dictionary with:
            - "error" (str): An error message.
    """
    
    session = get_session()
    if session:
        print('conected to data base')
    
    if not session:
        return jsonify({"error": "Error connecting to the database"}), 500

    try:
        result_query = session.query(Taxis)

        if plate:
            result_query = result_query.filter(Taxis.plate == plate)

        # Implement pagination
        if page and limit:
            # Suponiendo que page = 2 y limit = 10
            # Calcula el número de resultados a omitir
            offset = (page - 1) * limit 
            
            # Si se aplica paginación
            result_query = result_query.offset(offset).limit(limit)

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