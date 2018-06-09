from aiohttp import web
from quedar.server import create_app

web.run_app(create_app())
