import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_get_weather():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/weather", params={"city": "Iasi"})
    
    assert response.status_code == 200

    json_data = response.json()
    assert "city" in json_data
    assert "temperature" in json_data
    assert "description" in json_data
    assert "timestamp" in json_data
