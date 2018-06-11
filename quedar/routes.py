from .views import health, get_group, post_group

async def setup_routes(app):
    app.router.add_get('/', health)
    app.router.add_get('/api/v1/group/{id}', get_group)
    app.router.add_post('/api/v1/group', post_group)
