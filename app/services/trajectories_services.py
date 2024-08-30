from app.database.db_sql import get_session
from app.models.trajectories import Trajectories


def fetch_trajectories(taxi_id, date_initial, date_end):
    print("------------------------------- fetch_trajectories")
    print(taxi_id, date_initial, date_end)
    session = get_session()
    
    if not session:
        return {"error": "Error connecting to the database"}, 500
    
    print('connected to database')
    
    try:
        result_query = session.query(Trajectories)

        if taxi_id and date_initial and date_end:
            result_query = result_query.filter(
                Trajectories.taxi_id == taxi_id,
                Trajectories.date >= date_initial,
                Trajectories.date <= date_end 
            )

        table_taxis = []

        for row in result_query:
            table_taxis.append(
                {
                "id": row.id,
                "taxi_id": row.taxi_id,
                "date": row.date,
                "latitude": row.latitude,
                "longitude": row.longitude
                }
            )
        
        if not table_taxis:
            return {"error": "No trajectories found."}, 404
            
        return table_taxis
        
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}, 500
        
    finally:
        session.close()
        print("Session closed")