guest_list = ["hitler", "stalin", "pol pot"]
#print(f"I would like to invite {guest_list[0].title()} to my birthday")
#print(f"I would like to invite {guest_list[1].title()} to my birthday")
#print(f"I would like to invite {guest_list[2].title()} to my birthday")

cant_make_it = "pol pot"
guest_list.remove(cant_make_it)
#print(f"I'm sad to hear {cant_make_it} cant come to my birthday")
guest_list.append("satan")

#print(f"I would like to invite {guest_list[2].title()} to my birthday party")
#print(f"It b with great joy that i got a new bitchin table, +1 if you wish {guest_list[0].title()}")

guest_list.insert(0, "jesus")
guest_list.insert(2, "Thrall")
guest_list.insert(-1, "Leo")
#print(f"I would like to invite {guest_list[0].title()} to my birthday party")
#print(f"I would like to invite {guest_list[1].title()} to my birthday party")
#print(f"I'm sorry {guest_list[2].title()}, i hate you now.")
#print(f"I'm sorry {guest_list[3].title()}, i hate you now.")
#print(f"I'm sorry {guest_list[4].title()}, i hate you now.")
#print(f"I'm sorry {guest_list[5].title()}, i hate you now.")

first_uninvite = guest_list.pop()
second_uninvite = guest_list.pop()
third_uninvite = guest_list.pop()
fourth_uninvite = guest_list.pop()
print(f"I am sorry {first_uninvite.title()}, i hate you now.")
print(f"I am sorry {second_uninvite.title()}, i hate you now.")
print(f"I am sorry {third_uninvite.title()}, i hate you now.")
print(f"I am sorry {fourth_uninvite.title()}, i hate you now.")

print(f"We still bois, come whenever! {guest_list[0].title()}")
print(f"We still bois, come whenever! {guest_list[1].title()}")

del guest_list[1]
del guest_list[0]
print(guest_list)

print(len(guest_list))