sandwich_orders = ["bbq chicken", "pastrami", "meatball", "ham and cheese", "pastrami", "tuna", "pastrami"]
finished_sandwiches = []

prompt = "\nWelcome to Subway"
prompt += "\nPlease choose your preferred sandwich"
no_ingredient = "pastrami"
print(f"{prompt}\n we have run out of {no_ingredient}")


while "pastrami" in sandwich_orders:
    sandwich_orders.remove('pastrami')



#loop through the list and print a message for each order
while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()

    print(f"I made your {current_sandwiches} sandwich.")
    finished_sandwiches.append(current_sandwiches)

print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)