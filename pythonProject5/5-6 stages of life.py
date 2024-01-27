age = 27
if age < 2:
    human = "baby"
elif age < 4:
    human = "toddler"
elif age < 13:
    human = "kid"
elif age < 20:
    human = "teenager"
elif age < 65:
    human = "adult"
else:
    human = "elder"
print(f"You are a {human}.")