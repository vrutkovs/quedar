async def test_get_group(client, loop):
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
