from .views import get_group

async def setup_routes(app):
    app.router.add_get('/api/v1/group/{id}', get_group)
