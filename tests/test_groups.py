import pytest
from quedar.server import create_app
from quedar.db import sample_data

@pytest.fixture
def app(loop):
    return create_app()

@pytest.fixture
async def client(test_client, app, loop):
    result = await test_client(app)
    await sample_data(app['engine'])
    return result

async def test_groups(client, loop):
    resp = await client.get('/group/1')
    assert resp.status == 200
    result = await resp.json()
    assert result == {
        "name": "Test group",
        "description": "Test group description",
        "country": "Czech Republic",
        "city": "Brno",
        "creator": 1
    }
