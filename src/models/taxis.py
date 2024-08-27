from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, Float, VARCHAR


# models taxis models.py
Base = DeclarativeBase()

class Taxis(Base):
    
    __tablename__="taxis"
    
    id = Column(Integer, primary_key=True)
    plate = Column(VARCHAR)
    trajectories = relationship("Trajectories", back_populates="taxis")