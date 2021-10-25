from pyramid.view import view_config
import db_json

# Returns history data
def fetch_history():
    data = db_json.fetch_data(json_str=True)
    print(type(data))
    return data


@view_config(route_name='home', renderer='ABCcalculator:templates/home.pt')
def home(request):
    data = fetch_history()
    return {'project': 'ABCcalculator',
            'data': data}

