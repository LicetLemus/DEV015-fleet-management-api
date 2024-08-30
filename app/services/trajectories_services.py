from app.database.db_sql import get_session
from app.models.trajectories import Trajectories
from app.utils.validation_session import validation_session


def fetch_trajectories(taxi_id, date_initial, date_end):
    """
    Gets trajectories for a taxi with taxi_id and date range from the database.

    Parameters:
    - taxi_id: ID of the taxi (string).
    - date_initial: Start date of the range in 'YYYY-MM-DD HH:MM:SS' format.
    - date_end: End date of the range in 'YYYY-MM-DD HH:MM:SS' format.

    Returns:
    - List of dictionaries with trajectory information if results are found.
    - Dictionary with an error message if no trajectories are found or if there is a problem.
    """
    
    print("------------------------------- fetch_trajectories")
    session = get_session()
    validation_session(session)
    
    try:
        # Start building the query
        result_query = session.query(Trajectories)
        result_query = get_query_with_params_trajectories(result_query, taxi_id, date_initial, date_end)
            
        # Prepare to collect the results
        trajectories_list = [
            {
                "id": row.id,
                "taxi_id": row.taxi_id,
                "date": row.date,
                "latitude": row.latitude,
                "longitude": row.longitude
            }
            for row in result_query
        ]
        
        # Check if no results were found
        if not trajectories_list:
            return {"error": "No trajectories found."}, 404
            
        return trajectories_list
        
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}, 500
        
    finally:
        session.close()
        print("Session closed")
        

def get_query_with_params_trajectories(result_query, taxi_id, date_initial, date_end):
    """
    Get result_query for taxi ID and date from the request.
    
    Return:
        - `taxi_id` (str): The ID of the taxi extracted from the query parameters.
        - `date_str` (str): The date string extracted from the query parameters.
    """
    if taxi_id and date_initial and date_end:
        return result_query.filter(
            Trajectories.taxi_id == taxi_id,
            Trajectories.date >= date_initial,
            Trajectories.date <= date_end 
        )
    return result_query
    