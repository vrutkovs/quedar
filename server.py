from aiohttp import web
from quedar.routes import setup_routes
from quedar.settings import config
from quedar.db import init_db

app = web.Application()
setup_routes(app)
app['config'] = config
init_db(app)
web.run_app(app)
