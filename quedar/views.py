from aiohttp import web
from . import db

async def index(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def fill_in_sample_data(request):
    await db.sample_data(db.engine)
    return web.Response(text="Sample data filled in")

async def group(request):
    async with db.engine.connect() as conn:
        group_id = request.match_info['id']
        try:
            result = await db.group.select(db.group.c.id == group_id)
            d_group =  await result.fetchone()
        except db.RecordNotFound as e:
            raise web.HTTPNotFound(text=str(e))
        return {
            'name': d_group.name,
            'description': d_group.description,
            'country': d_group.country,
            'city': d_group.city,
            'creator': d_group.creator,
        }
