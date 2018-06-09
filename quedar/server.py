from aiohttp import web
from .routes import setup_routes
from .settings import set_config
from .db import init_db

def create_app():
    app = web.Application()
    app.on_startup.append(set_config)
    app.on_startup.append(setup_routes)
    app.on_startup.append(init_db)
    return app
