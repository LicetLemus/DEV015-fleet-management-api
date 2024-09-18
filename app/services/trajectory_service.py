from app.database.db_sql import db
from app.models.trajectories import Trajectories


def fetch_trajectories(taxi_id, date_initial, date_end):
    """
    Retrieves trajectories for a taxi within a date range.

    Args:
        taxi_id (str): Taxi ID.
        date_initial (str): Start date ('YYYY-MM-DD HH:MM:SS').
        date_end (str): End date ('YYYY-MM-DD HH:MM:SS').

    Returns:
        tuple: (List of trajectories or error message, HTTP status code)
            - 200: Success with data.
            - 404: No data found.
            - 500: Server error.
    """

    print("------------------------------- fetch_trajectories")

    try:
        # Initialize the query
        query = db.session.query(Trajectories)

        if taxi_id and date_initial and date_end:
            query = query.filter(
                Trajectories.taxi_id == taxi_id,
                Trajectories.date >= date_initial,
                Trajectories.date <= date_end,
            )

        print("query----------------", query)

        # Execute the query and fetch results
        trajectories_results = query.all()
        print("result---------------", trajectories_results)

        # Build the response
        if not trajectories_results:
            print("Entrance if-------------")
            return {"error": "No trajectories found."}, 404

        # Prepare to response the results
        response = [
            {
                "id": trajectory.id,
                "taxiId": trajectory.taxi_id,
                "date": trajectory.date,
                "latitude": trajectory.latitude,
                "longitude": trajectory.longitude,
            }
            for trajectory in trajectories_results
        ]

        return response, 200

    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}, 500
    
    finally:
        db.session.close()
        print("Session closed")
