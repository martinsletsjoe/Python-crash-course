sandwich_orders = ["bbq chicken", "meatball", "ham and cheese", "tuna"]
finished_sandwiches = []


#loop through the list and print a message for each order
while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()

    print(f"I am making your {current_sandwiches} sandwich.")
    finished_sandwiches.append(current_sandwiches)

print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)