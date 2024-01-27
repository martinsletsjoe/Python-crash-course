#make an empty list for storing aliens.
aliens = []

#make 30 green aliens.
for alien_number in range(30):
    new_alien = {"colour": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

#show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
#show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[:6]:
    if alien["colour"] == "green":
        alien["colour"] ="yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["colour"] == "yellow":
        alien["colour"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15
for alien in aliens[:6]:
    print(alien)