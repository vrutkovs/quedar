from aiohttp import web
from quedar.routes import setup_routes
from quedar.settings import config

app = web.Application()
setup_routes(app)
app['config'] = config
web.run_app(app)
