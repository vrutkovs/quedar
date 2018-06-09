from .views import index, sample_data, get_group

async def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/group/{id}', get_group)
