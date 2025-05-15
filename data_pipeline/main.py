import requests
from models import Weather, Base
from db.db import engine, SessionLocal
from config import OPENWEATHER_API_KEY

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }

def main():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

    cities = ["London", "New York", "Tokyo"]
    session = SessionLocal()
    try:
        for city in cities:
            weather_data = fetch_weather(city)
            weather = Weather(
                city=weather_data["city"],
                temperature=weather_data["temperature"],
                description=weather_data["description"]
            )
            session.add(weather)
            print(f"Added weather data for {city}: {weather_data}")
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    main()
