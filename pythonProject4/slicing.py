players = ["charles", "martina", "michael", "florence", "eli"]
#print(players[0:4])
#print(players[-3::2])

print("Here are the first three player on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are")
print(friend_foods)