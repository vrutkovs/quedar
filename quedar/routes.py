from .views import index, sample_data, group_handler

async def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/group/{id}', group_handler)
