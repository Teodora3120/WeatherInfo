import httpx
from app.models import Weather
from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from app.config import OPENWEATHER_API_KEY, OPENWEATHER_API_URL
from datetime import datetime

async def fetch_weather(city: str):
    url = f"{OPENWEATHER_API_URL}?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    }


async def get_weather_data(city: str):
    session: Session = SessionLocal()
    try:
        weather_data = await fetch_weather(city)
        existing = session.query(Weather).filter(Weather.city == city).first()

        if existing:
            existing.temperature = weather_data["temperature"]
            existing.description = weather_data["description"]
            existing.timestamp = datetime.utcnow()
            session.commit()
            session.refresh(existing)
            return {
                "city": existing.city,
                "temperature": existing.temperature,
                "description": existing.description,
                "timestamp": existing.timestamp,
            }
        else:
            weather = Weather(**weather_data)
            session.add(weather)
            session.commit()
            session.refresh(weather)
            return {
                "city": weather.city,
                "temperature": weather.temperature,
                "description": weather.description,
                "timestamp": weather.timestamp,
            }
    except Exception as e:
        session.rollback()
        return {"error": str(e)}
    finally:
        session.close()
