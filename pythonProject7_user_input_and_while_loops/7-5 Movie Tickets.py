while True:
    age = input("What is your age? ")
    if not age.isdigit():
        print("\tWrong input")
    elif int(age) < 3:
        print("\tYour ticket is free.")
    elif int(age) <= 12:
        print("\tYour ticket is 10$")
    else:
        print("\tYour ticket is 15$")