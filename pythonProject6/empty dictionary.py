# alien_0 = {}
# alien_0["colour"] = "green"
# alien_0["points"] = 5
# print(f"The alien is {alien_0['colour']}")
# alien_0["colour"] = "yellow"
# print(f"The alien is now {alien_0['colour']}")

alien_0 = {"x_position": 0,"y_position":25, "speed": "medium"}
print(f"Original position: {alien_0['x_position']}")
#move the alien to the right.
#Determine how far to move the alien based on its current speed.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0 ["speed"] == "fast":
    x_increment = 2
else:
    #This must be a fast alien.
    x_increment = 3

#The new position is the old position pls the increment.
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New position: {alien_0['x_position']}")