# prompt = "If you could visit one place in the world, where would you go?"

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat != 'yes':
        polling_active = False

print("\n--- Poll results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")