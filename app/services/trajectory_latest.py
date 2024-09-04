from app.database.db_sql import get_session
from sqlalchemy import func
from app.models.trajectories import Trajectories
from app.utils.validation_session import validation_session


def fetch_trajectory_latest():
    session = get_session()
    validation_session(session)
    
    try:
        # Initialize the subquery to find the latest date for each taxi
        subquery = (session.query(
            Trajectories.taxi_id,
            func.max(Trajectories.date).label('latest_date')
        )
        .group_by(Trajectories.taxi_id)
        .subquery()
        )
        
        # Main query to join Trajectories with the subquery
        query = (
        session.query(Trajectories)
        .join(subquery, (Trajectories.taxi_id == subquery.c.taxi_id) & (Trajectories.date == subquery.c.latest_date))
        .all()
        )
        
        print('subquery----------------', subquery)
        
        # Build the response
        if not query:
            print('entrada if-------------')
            return {"error": "No trajectories found."}, 404
        
        # Prepare to collect the results
        trajectory_list = [
            {
            "taxi_id": trajectory.taxi_id,
            "date": trajectory.date,
            "latitude": trajectory.latitude,
            "longitude": trajectory.longitude
            }
            for trajectory in query
        ]
        
        response = {
            "total_trajectories": len(trajectory_list),
            "trajectories": trajectory_list
        }
        
        print('trajectories list-------------', response)

        return response, 200
        
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}, 500
        
    finally:
        session.close()
        print("Session closed")