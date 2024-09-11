from app.database.db_sql import db  # Importa el objeto db configurado en __init__.py
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship


class Taxis(db.Model):
    """
    SQLAlchemy ORM model for the 'taxis' table.

    Attributes:
    - id (int): Primary key of the taxi record.
    - plate (str): License plate number of the taxi.
    - trajectories (relationship): One-to-many relationship with the 'Trajectories' model.

    Example:
        new_taxi = Taxis(id=1, plate='ABC123')
    """

    __tablename__ = "taxis"

    id = Column(Integer, primary_key=True)
    plate = Column(VARCHAR)
    trajectories = relationship("Trajectories", back_populates="taxis")
