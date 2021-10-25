from pyramid.view import ( view_config, view_defaults )
from getBMI import BMI
from datetime import date, datetime
from dbconnect import add_to_history


# http://localhost:6543/

@view_defaults(route_name='bmi_calculator')
class TutorialView1:
    def __init__(self, request):
        self.request = request

    # BMI Calculator

    @view_config(route_name='bmi_calculator', renderer='ABCcalculator:templates/bmi_home.pt')
    def bmi_home(self):
        return{}

    @view_config(request_method='POST', renderer='ABCcalculator:templates/getBmi.pt')
    def getBmi(self):
        height = self.request.params['height']
        weight = self.request.params['weight']

        height = float(height)
        weight = float(weight)

        bmi = BMI(height, weight)

        add_to_history(datetime.now().strftime("%d-%m-%Y %H:%M:%S"), f"H: {height} m | W: {weight} kg | BMI: {bmi['value']} | status: {bmi['msg']}")

        # {'value': 21.64532402096181, 'msg': 'Healthy'}
        return{
            'bmi': bmi,
        }