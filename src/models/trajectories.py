from sqlalchemy import Column, Integer, TIMESTAMP, Double, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

Base = DeclarativeBase()

class Trajectories(Base):
    __tablename__= "trajectories"
    
    id = Column(Integer, primary_key=True)
    taxi_id = Column(Integer, ForeignKey('taxis_id'))
    date = Column(TIMESTAMP)
    latitude = Column(Double)
    longitude = Column( Double)
    taxis = relationship("Taxis", back_populates="trajectories")