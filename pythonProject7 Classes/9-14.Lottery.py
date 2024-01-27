from random import choice
possibilities = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']


num_rolls = 4
winning_ticket = []
my_ticket = 'a'
print(f"Any tickets matching these four numbers or letters wins a prize!")

# while len(winning_ticket) < 4:
#
#     pulled_item = choice(possibilities)
#     if pulled_item not in winning_ticket:
#         print(f" We pulled a {pulled_item}!")
#         winning_ticket.append(pulled_item)

count = 0
while len(winning_ticket) < 100:
    count += 1
    pulled_item = choice(possibilities)
    if pulled_item not in winning_ticket:
        print(f" We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)
    if pulled_item == 'a':
        break
print(f"{count} attempts before you won!")



# for winner in range(num_rolls):
#     results = choice(mixed)
#     print(results)
#
