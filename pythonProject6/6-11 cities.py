cities = {
    "sandefjord": {
        "country": "norway",
        "population": 60_000,
        "county": "vestfold",
    },
    "paris": {
        "country": "france",
        "population": 2_000_000,
        "county": "Île-de-France",
    },
    "stockholm": {
        "country": "sweden",
        "population": 1_000_000,
        "county": "stockholm county"
    }
}

for city, cityinfo in cities.items():
    print(f"\n{city}")
    country = f"{cityinfo['country'].title()}"
    population = f"\t{cityinfo['population']}"
    county = f"\t{cityinfo['county']}"

    # print(country)
    # print(population)
    # print(county)
    print(f"The city of {city} is in the country {country}."
          f" It has a population of{population} people and is in the county{county}")