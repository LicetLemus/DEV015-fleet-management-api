from app.database.db_sql import get_session
from app.models.trajectories import Trajectories


def fetch_trajectories(taxi_id, date_initial, date_end):
    """
    Gets trajectories for a taxi with taxi_id and date range from the database.

    Parameters:
    - taxi_id: ID of the taxi (string).
    - date_start: Start date of the range in 'YYYY-MM-DD HH:MM:SS' format.
    - date_end: End date of the range in 'YYYY-MM-DD HH:MM:SS' format.

    Returns:
    - List of dictionaries with trajectory information if results are found.
    - Dictionary with an error message if no trajectories are found or if there is a problem.

    Exceptions:
    - Raises an exception if there is an error connecting to the database or during the query.

    Returns:
    - List or dict: List of trajectories or dictionary with an error message.
    """
    
    print("------------------------------- fetch_trajectories")
    print(taxi_id, date_initial, date_end)
    session = get_session()
    
    if not session:
        return {"error": "Error connecting to the database"}, 500
    
    print('connected to database')
    
    try:
        # Start building the query
        query = session.query(Trajectories)

        if taxi_id and date_initial and date_end:
            # Filter results based on taxi_id and date range
            query = query.filter(
                Trajectories.taxi_id == taxi_id,
                Trajectories.date >= date_initial,
                Trajectories.date <= date_end 
            )
            
        # Prepare to collect the results
        trajectories_list = []

        for row in query:
            trajectories_list.append(
                {
                "id": row.id,
                "taxi_id": row.taxi_id,
                "date": row.date,
                "latitude": row.latitude,
                "longitude": row.longitude
                }
            )
        
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