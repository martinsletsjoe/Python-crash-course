players = ["charles", "martina", "michael", "florence", "eli"]
print("The first three items in the list are:")
for player in players[:3]:
    print(player.title())


my_foods = ["pizza", "falafel", "carrot cake", "chocolate cake", "ice cream", "sorbet"]
my_foods.append("panacotta")
print("\nthree items from the middle of the list are:")
for my_food in my_foods[1:-3]:
    print(my_food.title())

print("\nThe last three items in the list are:")
for my_food in my_foods[-4:-1]:
    print(my_food)