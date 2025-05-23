from pydantic import BaseModel
from datetime import datetime
from typing import Union

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    description: str
    wind_speed: float
    wind_deg: Union[int, None]
    timestamp: datetime

    class Config:
        orm_mode = True
