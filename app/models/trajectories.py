from sqlalchemy import Column, Integer, TIMESTAMP, Double, ForeignKey
from app.database.db_sql import db
from sqlalchemy.orm import relationship


class Trajectories(db.Model):
    """
    SQLAlchemy ORM model for the 'trajectories' table.

    Attributes:
    - id (int): Primary key of the trajectory record.
    - taxi_id (int): Foreign key referencing the 'taxis' table.
    - date (datetime): Timestamp of the trajectory.
    - latitude (float): Latitude of the trajectory.
    - longitude (float): Longitude of the trajectory.
    - taxis (relationship): Many-to-one relationship with the 'Taxis' model.

    Example:
        new_trajectory = Trajectories(
            id=1,
            taxi_id=1,
            date=datetime.utcnow(),
            latitude=12.345,
            longitude=67.890
        )
    """

    __tablename__ = "trajectories"

    id = Column(Integer, primary_key=True)
    taxi_id = Column(Integer, ForeignKey("taxis.id"))
    date = Column(TIMESTAMP)
    latitude = Column(Double)
    longitude = Column(Double)
    taxis = relationship("Taxis", back_populates="trajectories")
