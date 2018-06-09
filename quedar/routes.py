from .views import index, sample_data

async def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/fill_in_sample_data', sample_data)
    app.router.add_get('/group/{id}', group)
