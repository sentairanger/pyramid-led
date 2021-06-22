from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('button', '/')
    config.add_route('ledon', '/ledon')
    config.add_route('ledoff', '/ledoff')
    config.scan('.views')
    return config.make_wsgi_app()