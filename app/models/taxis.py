from sqlalchemy.orm import relationship
from app.models import Base
from sqlalchemy import Column, Integer, VARCHAR
from app.models import trajectories

class Taxis(Base):
    """
    SQLAlchemy ORM model for the 'taxis' table.

    Attributes:
    - id (int): Primary key of the taxi record.
    - plate (str): License plate number of the taxi.
    - trajectories (relationship): One-to-many relationship with 'Trajectories'.

    Usage:
    Create a new taxi:
    ```python
    new_taxi = Taxis(id=1, plate='ABC123')
    ```
    """
    
    __tablename__="taxis"
    
    id = Column(Integer, primary_key=True)
    plate = Column(VARCHAR)
    trajectories = relationship("Trajectories", back_populates="taxis")