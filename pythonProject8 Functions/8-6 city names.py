def city_country(city, country):
    '''return city-country pairs and print values that are returned'''
    country_info = f"{city}, {country}"
    return country_info.title()

pair = city_country('santiago', 'chile')
print(pair)
pair = city_country('sandefjord', 'norway')
print(pair)
pair = city_country('london', 'england')
print(pair)