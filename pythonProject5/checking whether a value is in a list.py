requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" and "pepperoni"in requested_toppings)
# print("pepperoni" in requested_toppings)

banned_user = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_user:
    print(f"{user.title()}, you can post a response if you wish")