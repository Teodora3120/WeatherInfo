import httpx
from datetime import datetime
from sqlalchemy.orm import Session
from app.models import Weather
from app.db.session import SessionLocal
from app.config import OPENWEATHER_API_KEY, OPENWEATHER_API_URL

async def fetch_weather(city: str):
    """Fetch weather data from the OpenWeather API."""
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
    """Get and save (or update) weather data for a city."""
    session: Session = SessionLocal()
    try:
        weather_data = await fetch_weather(city)

        existing = session.query(Weather).filter_by(city=city).first()

        if existing:
            # Update existing record
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
            # Insert new record
            new_weather = Weather(
                city=weather_data["city"],
                temperature=weather_data["temperature"],
                description=weather_data["description"],
                timestamp=datetime.utcnow()
            )
            session.add(new_weather)
            session.commit()
            session.refresh(new_weather)

            return {
                "city": new_weather.city,
                "temperature": new_weather.temperature,
                "description": new_weather.description,
                "timestamp": new_weather.timestamp,
            }

    except Exception as e:
        session.rollback()
        return {"error": str(e)}
    finally:
        session.close()
