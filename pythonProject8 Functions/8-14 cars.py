# def cars(manufacturer, model_name, **optional_features):
#     '''build a dictionary containing information about a car'''
#     optional_features['car_brand'] = manufacturer
#     optional_features['car_model'] = model_name
#     return optional_features
#
# user_car = cars('subaru', 'outback',
#                 color='blue',
#                 tow_package=True)
#
# print(user_car)
def make_car(manufacturer, model, **options):
    '''Make a dictionary representing a car'''
    car_dict= {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', colour='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, colour='white', headlights='popup')
print(my_old_accord)