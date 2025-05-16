from fastapi import APIRouter, Query, HTTPException
from app.services.weather_service import get_weather_data
from app.schemas import WeatherResponse

router = APIRouter()

@router.get("/weather", response_model=WeatherResponse)
async def get_weather(city: str = Query(..., description="City to fetch weather for")):
    print("City", city)
    result = await get_weather_data(city)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result