filename = 'guest.txt'

prompt = input("What is your name?")
with open(filename, 'w') as file_object:
    file_object.write(prompt)
