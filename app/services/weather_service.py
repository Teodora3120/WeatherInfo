import httpx
from app.models import Weather
from app.db.session import SessionLocal
from app.config import OPENWEATHER_API_KEY, OPENWEATHER_API_URL

async def fetch_weather(city: str):
    url = f"{OPENWEATHER_API_URL}?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }

async def get_weather_data(city: str):
    session = SessionLocal()
    try:
        weather_data = await fetch_weather(city) 
        weather = Weather(**weather_data)
        session.add(weather)
        session.commit()
        return weather_data
    except Exception as e:
        session.rollback()
        return {"error": str(e)}
    finally:
        session.close()
