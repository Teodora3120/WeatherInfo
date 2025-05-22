import pytest
from app.main import app
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_get_weather():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/weather", params={"city" : "Iasi"})
    assert response.status_code == 200

    json_data = response.json()
    assert "city" in json_data
    assert "temperature" in json_data
    assert "description" in json_data
    assert "timestamp" in json_data