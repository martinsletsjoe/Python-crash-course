pets = []

catto = {
    "species": "cat",
    "owner": "lars",
    "colour": "tabby",
}
pets.append(catto)

doggo = {
    "species": "dog",
    "owner": "kevin",
    "colour": "brown",
}
pets.append(doggo)

birdo = {
    "species": "bird",
    "owner": "paul",
    "colour": "blue"
}
pets.append(birdo)

for animals in pets:
    species = animals["species"].title()
    owner = animals["owner"].title()
    colour = animals["colour"].title()

    print(f"{owner}'s pet is a {colour} {species}")

#this is how the solution does it
# pet = {
#     'animal type': 'dog',
#     'name': 'peso',
#     'owner': 'eric',
#     'weight': 37,
#     'eats': 'shoes',
# }
# pets.append(pet)
#
# # Display information about each pet.
# for pet in pets:
#     print(f"\nHere's what I know about {pet['name'].title()}:")
#     for key, value in pet.items():
#         print(f"\t{key}: {value}")