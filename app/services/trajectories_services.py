from app.database.db_sql import get_session
from flask import jsonify
from app.models.trajectories import Trajectories


def fetch_trajectories(taxi_id, date):
    print("------------------------------- fetch_trajectories")
    session= get_session()
    
    if not session:
        return jsonify({"error": "Error connecting to the database"}), 500
    
    print('connected to database')
    
    try:
        result_query = session.query(Trajectories)

        if taxi_id and date:
            result_query = result_query.filter(
                Trajectories.taxi_id == taxi_id, 
                Trajectories.date == date
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
        return jsonify({"Error": str(e)})
        
    finally:
        session.close()
        print("Session closed")