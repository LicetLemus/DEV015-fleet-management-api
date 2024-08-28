from sqlalchemy.orm import relationship
from app.models import Base
from sqlalchemy import Column, Integer, VARCHAR
from app.models import trajectories

class Taxis(Base):
    
    __tablename__="taxis"
    
    id = Column(Integer, primary_key=True)
    plate = Column(VARCHAR)
    trajectories = relationship("Trajectories", back_populates="taxis")