# car_brand = input("What kind of rental car would you like? ")
# print(f"Let me see if I can find you a {car_brand}.")

# party = input("How many people are in your group? ")
# party = int(party)
# if party > 8:
#     print("\nYou will have to wait for a table.")
# else:
#     print("\nFollow me")

number = input("Write and number and I will report whether the number is a multiple of 10 or not. ")
number = int(number)

if number % 10 == 0:
    print("You're number is a multiple of 10.")
else:
    print(f"you're number {number} is not a multiple of 10.")