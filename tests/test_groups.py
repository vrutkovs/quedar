async def test_get_group(client, loop):
    resp = await client.get('/api/v1/group/1')
    assert resp.status == 200
    result = await resp.json()
    assert result == {
        "name": "Test group",
        "description": "Test group description",
        "country": "Czech Republic",
        "city": "Brno",
        "creator": 1
    }

async def test_post_group(client, loop):
    data = {
        "name": "Test group",
        "description": "Test group description",
        "country": "Czech Republic",
        "city": "Brno",
        "creator": 1
    }
    resp = await client.post('/api/v1/group', data=data)
    assert resp.status == 200
    result = await resp.json()
    # 'key' element would contain new group ID
    inserted_key = result['key']
    del result['key']
    assert result == {'status': 'ok'}

    resp = await client.get(f'/api/v1/group/{inserted_key}')
    assert resp.status == 200
    result = await resp.json()
    assert result == data
