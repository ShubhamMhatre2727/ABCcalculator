from pyramid.view import view_config


@view_config(route_name='weight_converter', renderer='ABCcalculator:templates/weight_converter.pt')
def weight_converter(request):
    return {'project': 'ABCcalculator'}
