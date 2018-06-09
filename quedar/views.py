from aiohttp import web
from .db import sample_data, group
from sqlalchemy.orm import sessionmaker


async def get_group(request):
    async with request.app['engine'].connect() as conn:
        group_id = request.match_info['id']
        result = await conn.execute(group.select(group.c.id == group_id))
        d_group = await result.fetchone()
        if d_group is None:
            raise web.HTTPNotFound(text="Not found")
        return web.json_response({
            'name': d_group.name,
            'description': d_group.description,
            'country': d_group.country,
            'city': d_group.city,
            'creator': d_group.creator,
        })
