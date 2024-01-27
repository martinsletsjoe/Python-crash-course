with open('learning_python.txt') as file_object:
    # contents = file_object.read()
    contents = file_object.read()
# print(contents)
# for content in contents:
#     print(content.rstrip())

# for i in range(3):
#     print(contents)

filename = 'learning_python.txt'

with open(filename) as file_object:
    # for line in file_object:
    #     print(line)
    lines = file_object.readlines()

for line in lines:
    line.strip()
    C = line.replace('Python', 'C')
    print(C.rstrip())

