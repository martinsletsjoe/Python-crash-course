import json

# favourite_number = input("What is your favourite number? ")

# filename = 'favourite_number.json'
#
# with open(filename, 'w') as f:
#     json.dump(favourite_number, f)
#     print(f"I know your favourite number! It's {favourite_number}")

def get_stored_favourite_number():
    '''Get stored favourite number if availabe.'''
    filename = 'favourite_number.json'
    try:
        with open(filename) as f:
            favourite_number = json.load(f)
    except FileNotFoundError:
        favourite_number = input("what is your favourite number? ")
        with open(filename, 'w') as f:
            json.dump(favourite_number, f)
    else:
        print(f"I know your favourite number! It's {favourite_number}")


get_stored_favourite_number()