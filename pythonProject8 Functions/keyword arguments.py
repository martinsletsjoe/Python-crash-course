# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# describe_pet(animal_type='hamster', pet_name='harry')

def describe_pet(pet_name, animal_type = 'dog'): #rekkefølgen her er viktig, default value må være sist, se s.135 andre paragraf.
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry')