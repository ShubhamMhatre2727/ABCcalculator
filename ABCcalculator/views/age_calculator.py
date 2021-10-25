from pyramid.view import view_config, view_defaults
from getAge import calculateAge
from datetime import date, datetime
from dbconnect import add_to_history


@view_defaults(route_name='age_calculator')
class TutorialView1:
    def __init__(self, request):
        self.request = request
        self.view_name = "Home Page"

    # Returns current date
    @property
    def current_date(self):
        return f"{date.today()}"

    @view_config(route_name='age_calculator', renderer='ABCcalculator:templates/age_home.pt')
    def age_home(request):
        return {}

    @view_config(request_method='POST', renderer='ABCcalculator:templates/getAge.pt')
    def dob(self):
        birth_date = self.request.params['birthday']
        data = calculateAge(birth_date)

        add_to_history(datetime.now().strftime("%d-%m-%Y %H:%M:%S"), f"DOB {birth_date} : {data['years']} years")

        return{
            'date': birth_date,
            "dob": data,
        }