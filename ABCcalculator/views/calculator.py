from pyramid.view import view_config


@view_config(route_name='calculator', renderer='ABCcalculator:templates/calculator.pt')
def calculator(request):
    return {'project': 'ABCcalculator'}


