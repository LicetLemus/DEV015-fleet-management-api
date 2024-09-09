from app.database.db_sql import get_session
from sqlalchemy import func
from app.models.trajectories import Trajectories
from app.models.taxis import Taxis
from app.utils.validation_session import validation_session


def fetch_trajectory_latest():
    session = get_session()
    validation_session(session)

    try:
        # Initialize the subquery to find the latest date for each taxi
        subquery = (
            session.query(
                Trajectories.taxi_id, func.max(Trajectories.date).label("latest_date")
            )
            .group_by(Trajectories.taxi_id)
            .subquery()
        )

        query = (
            session.query(
                Taxis.id,
                Trajectories.latitude,
                Trajectories.longitude,
                Taxis.plate,
                Trajectories.date,
            )
            # .join(target, onclause)
            # target: The table or entity to which you want to join the parent table.
            # onclause: The condition upon which the join is made. Generally, it is an expression that indicates how the rows in the two tables are related.
            .join(
                Taxis, Trajectories.taxi_id == Taxis.id
            )  # foreignKey taxi_id = Column(Integer, ForeignKey('taxis.id'))
            .join(
                subquery,
                (Trajectories.taxi_id == subquery.c.taxi_id)
                & (Trajectories.date == subquery.c.latest_date),
            )
            .distinct()  #  .distinct() method remove duplicates in query result
        )

        print("Main Query SQL:", str(query))

        # Execute the query
        trajectories_latest_result = query.all()

        # Build the response
        if not trajectories_latest_result:
            return {"error": "No trajectories found."}, 404

        # Prepare to collect the results
        response = [
            {
                "taxiId": trajectory.id,
                "latitude": trajectory.latitude,
                "longitude": trajectory.longitude,
                "plate": trajectory.plate,
                "timestamp": trajectory.date,
            } 
            for trajectory in trajectories_latest_result
        ]

        return response, 200

    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}, 500

    finally:
        session.close()
        print("Session closed")
