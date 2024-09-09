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
        # Initialize the query
        query = session.query(Trajectories)

        if taxi_id and date_initial and date_end:
            query = query.filter(
                Trajectories.taxi_id == taxi_id,
                Trajectories.date >= date_initial,
                Trajectories.date <= date_end,
            )

        print("query----------------", query)

        # Execute the query and fetch results
        trajectories_results = query.all()
        print("resultado---------------", trajectories_results)

        # Build the response
        if not trajectories_results:
            print("entrada if-------------")
            return {"error": "No trajectories found."}, 404

        # Prepare to response the results
        response = [
            {
                "id": trajectorie.id,
                "taxiId": trajectorie.taxi_id,
                "date": trajectorie.date,
                "latitude": trajectorie.latitude,
                "longitude": trajectorie.longitude,
            }
            for trajectorie in trajectories_results
        ]

        return response, 200

    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}, 500

    finally:
        session.close()
        print("Session closed")
