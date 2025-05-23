from fastapi import APIRouter, Query, HTTPException
from app.services.weather_service import get_weather_data
from app.schemas import WeatherResponse
from app.db.session import SessionLocal
from app.models import Weather
from typing import List
from sqlalchemy import desc

router = APIRouter()

@router.get("/weather", response_model=WeatherResponse)
async def get_weather(city: str = Query(..., description="City to fetch weather for")):
    result = await get_weather_data(city)
    if isinstance(result, dict) and "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@router.get("/weather/all", response_model=List[WeatherResponse])
async def list_all_weather():
    session = SessionLocal()
    try:
        return session.query(Weather).order_by(desc(Weather.timestamp)).all()
    finally:
        session.close()
