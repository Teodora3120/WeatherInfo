from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Weather(Base):
    __tablename__ = "weather"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String, unique=True, nullable=False)
    temperature = Column(Float, nullable=False)
    feels_like = Column(Float, nullable=False)
    temp_min = Column(Float, nullable=False)
    temp_max = Column(Float, nullable=False)
    pressure = Column(Integer, nullable=False)
    humidity = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    wind_speed = Column(Float, nullable=False)
    wind_deg = Column(Integer, nullable=True)
    timestamp = Column(DateTime(timezone=True), default=datetime.now(tz=None))

    def __repr__(self):
        return f"id: {self.id}, name: {self.city}"


   
