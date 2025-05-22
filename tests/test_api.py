import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch
from app.main import app

# Define a fake weather response
mock_weather_response = {
    "city": "Iasi",
    "temperature": 22.5,
    "description": "clear sky",
    "timestamp": "2025-05-22T12:00:00Z"
}

# Patch the actual fetch_weather function used by the API
@pytest.mark.asyncio
@patch("app.services.weather_service.fetch_weather", return_value=mock_weather_response)
async def test_get_weather(mock_fetch_weather):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/weather", params={"city": "Iasi"})

    print(response)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["city"] == "Iasi"
    assert "temperature" in json_data
    assert "description" in json_data
    assert "timestamp" in json_data
