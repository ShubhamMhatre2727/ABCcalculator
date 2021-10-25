from pyramid.view import view_config

@view_config(route_name='about', renderer='ABCcalculator:templates/contact.pt')
def about(request):
    return {}

