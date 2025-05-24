# WeatherInfo

Welcome to **WeatherInfo**!  
This project is the engine behind a sleek weather web app, built with **Python**, **FastAPI**, **PostgreSQL**, and **Docker**. Whether you’re curious about today’s forecast or want to dig into historical weather trends, WeatherInfo has you covered.

> 🌐 **Check it out live:** [WeatherInfo Web App](https://v0-react-weather-app-sepia.vercel.app/)

## 🌦️ What’s Inside?

- Super-fast REST API powered by FastAPI
- Reliable data storage with PostgreSQL
- Hassle-free deployment using Docker
- Secure, production-ready setup
- Real-time and historical weather data

## 🚀 Get Started

### What You’ll Need

- Python 3.8 or newer
- Docker & Docker Compose

### Quick Start

Clone this repo and use the handy scripts to get things running:

```bash
python scripts/manage.py build  # Build Docker images
python scripts/manage.py up     # Start all services
python scripts/manage.py run    # Start FastAPI
python scripts/manage.py down   # Stop all services
python scripts/manage.py restart   # Restart all services
python scripts/manage.py makemigrations -m ''   # Creates the migration files
python scripts/manage.py migrate   # Applies the migrations

```

Once it’s up, your API lives at `http://localhost:8000`.

## 📚 API Docs

Explore and test the API right in your browser at  
`http://localhost:8000/docs`.

## 🛠️ Tech Stack

- **Python** & **FastAPI** – For the backend magic
- **PostgreSQL** – To keep your data safe
- **Docker** – For easy setup and scaling
- **Docker Compose** – To orchestrate everything

## 🌍 Try the Web App

See WeatherInfo in action:  
👉 [https://v0-react-weather-app-sepia.vercel.app/](https://v0-react-weather-app-sepia.vercel.app/)

## 📄 License

MIT License – free to use, share, and improve.


