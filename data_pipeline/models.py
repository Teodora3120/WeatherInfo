from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True)
    city = Column(String(50), nullable=False)
    temperature = Column(Float, nullable=False)
    description = Column(String(255))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
