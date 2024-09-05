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
                Trajectories.latitude,
                Trajectories.longitude,
                Trajectories.date,
                Trajectories.taxi_id,
                Taxis.plate,
                Taxis.id,
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

        # print("Main Query SQL:", str(subquery))

        # Execute the query
        trajectories_latest_result = query.all()

        # Build the response
        if not trajectories_latest_result:
            return {"error": "No trajectories found."}, 404

        # Prepare to collect the results
        trajectories_latest_list = [
            {
                "id": trajectory.id,
                "plate": trajectory.plate,
                "taxi_id": trajectory.taxi_id,
                "date": trajectory.date,
                "latitude": trajectory.latitude,
                "longitude": trajectory.longitude,
            }
            for trajectory in trajectories_latest_result
        ]

        response = {
            "total_trajectories": len(trajectories_latest_list),
            "trajectories": trajectories_latest_list,
        }

        print("Trajectories List:", response)

        return response, 200

    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}, 500

    finally:
        session.close()
        print("Session closed")
