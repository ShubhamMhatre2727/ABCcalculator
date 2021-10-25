def includeme(config):
    config.add_static_view('static', 'static')
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('calculator', '/calculator')
    config.add_route('age_calculator', '/age_calculator')
    config.add_route('bmi_calculator', '/bmi_calculator')
    config.add_route('weight_converter', '/weight_converter')
