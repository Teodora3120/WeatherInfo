import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME", "weather_data")
DB_USER = os.getenv("DB_USER", "weather_user")
DB_PASS = os.getenv("DB_PASS", "weather_pass")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
