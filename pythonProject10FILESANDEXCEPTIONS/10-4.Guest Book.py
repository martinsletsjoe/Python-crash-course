filename = 'guest_book.txt'



# with open(filename, 'a') as file_object:
#     while prompt == (''):
#         file_object.write(f"Visitor: {prompt.title()}\n")
#
# print(f"Hello {prompt}")
# with open(filename, 'a') as file_object:
#     file_object.write(f"Visitor: {prompt.title()}\n")
#
# print(f"Hello {prompt}")

fucksake = ''
while fucksake == '':
    prompt = input('Please enter your name: ')
    fucksake = prompt
with open(filename, 'a') as file_object:
    file_object.write(f"Visitor name: {prompt.title()}\n")

print(f"Hi {fucksake}!")