prompt = "\nPlease enter your wanted pizza toppings: "
prompt +="\nEnter 'quit when you are finished. "

num_toppings = 5
toppings_count = 0

active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        break

    elif toppings_count < num_toppings:
        print("adding " + topping + " to your pizza!")
        toppings_count += 1
    else:
        print("maximum number of toppings reached!")
        active = False
print("thank you for ordering from our pizza restaurant!")



