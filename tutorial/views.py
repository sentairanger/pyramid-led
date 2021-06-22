from pyramid.view import view_config

@view_config(route_name='button', renderer='home.pt')
def home(request):
    return {}

