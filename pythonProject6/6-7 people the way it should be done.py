#make an empty list to store people in.
people = []

person = {
    "first_name": "martin",
    "last_name": "sletsjøe",
    "age": 28,
    "city": "bærum",
}
people.append(person)

person = {
    "first_name": "lemmy",
    "last_name": "matthes",
    "age": 2,
    "city": "sitka",
}

people.append(person)

person = {
    "first_name": "willie",
    "last_name": "matthes",
    "age": 11,
    "city": "sitka",
}

people.append(person)

#display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person["age"]
    city = person["city"].title()

    print(f"{name}, of {city}, is {age} years old.")