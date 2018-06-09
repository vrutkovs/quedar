from .views import get_group

async def setup_routes(app):
    app.router.add_get('/group/{id}', get_group)
