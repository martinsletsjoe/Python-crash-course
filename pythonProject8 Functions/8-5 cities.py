def describe_city(city, country = 'Iceland'):
    '''Display information about what country the city is in'''
    print(f"{city.title()} is in {country.title()}.")

describe_city('reykjavik')
describe_city('larvik', country='Norway')
describe_city('paris', 'france')