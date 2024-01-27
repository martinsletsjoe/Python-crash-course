people = {
    "fish": {
        "first": "martin",
        "last": "sletsjøe",
        "age": 28,
        "city": "bærum"
    },
    "lesh": {
        "first": "Lars",
        "last": "fredriksen",
        "age": 30,
        "city": "tønsberg"
    },
    "sokken": {
        "first": "leo",
        "last": "sundstøl",
        "age": 27,
        "city": "sandefjord"
    },
}

for username, user_info in people.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    age = user_info['age']
    city = user_info['city']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tAge: {age}")
    print(f"\tCity: {city.title()}")






