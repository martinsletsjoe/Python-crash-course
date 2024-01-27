pizzas = ["kebab", "pepperoni", "taco"]
for pizza in pizzas:
    print(f"Jeg er så veldig glad i {pizza} pizza")
print("I really love pizza!\nPizza is pogchamp\n")

friend_pizzas = pizzas[:]
pizzas.append("macaroni")
friend_pizzas.append("ananas")

print("my favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)


#Jeg har brukt for loop hele veien, ops?
my_foods = ["pizza", "falafel", "carrot cake", "chocolate cake", "ice cream", "sorbet"]
my_foods.append("panacotta")
print("\nthese items are from the middle of the list are:")
print(my_foods[1:-2])


#birbs = ["spurv", "blåmeis", "dompap"]
#for birb in birbs:
 #   print(f"Farmor er veldig glad i å mate {birb} på balkongen.")
  #  print(f"Jeg vet ikke om Farmor har sett {birb} nære på.")