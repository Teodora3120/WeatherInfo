from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.models import Weather
from app.db.session import SessionLocal
from app.config import OPENWEATHER_API_KEY, OPENWEATHER_API_URL
from datetime import datetime
import httpx

async def fetch_weather(city: str):
    url = f"{OPENWEATHER_API_URL}?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "pressure": data["main"]["pressure"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
        "wind_deg": data["wind"].get("deg")
    }

async def get_weather_data(city: str):
    session: Session = SessionLocal()
    weather_data = await fetch_weather(city)
    try:
        # First, try to insert new row
        new_weather = Weather(**weather_data, timestamp=datetime.utcnow())
        session.add(new_weather)
        session.commit()
        session.refresh(new_weather)
        return new_weather

    except IntegrityError:
        # If duplicate, update existing
        session.rollback()
        existing = session.query(Weather).filter_by(city=city).first()
        if existing:
            for field, value in weather_data.items():
                setattr(existing, field, value)
            existing.timestamp = datetime.utcnow()
            session.commit()
            session.refresh(existing)
            return existing

        return {"error": "Failed to insert or update weather record."}

    except Exception as e:
        session.rollback()
        return {"error": str(e)}

    finally:
        session.close()
