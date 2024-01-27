def get_formatted_city(city_name, country_name='', population=''):
    '''Generate a neatly formatted string of the form City, Country'''
    if population:
        full_info = f"{city_name}, {country_name} - {population}."
    elif country_name:
        full_info = f"{city_name}, {country_name}."
    else:
        full_info = f"{city_name}."
    return full_info.title()

    # full_info = f"{city_name}, {country_name}"
    # return full_info.title()
