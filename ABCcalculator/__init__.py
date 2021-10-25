from pyramid.config import Configurator
import dbconnect

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_chameleon')
        config.include('.routes')
        config.add_static_view(name='static', path='ABCcalculator:static')
        config.scan()
    dbconnect.table_init()
    return config.make_wsgi_app()
