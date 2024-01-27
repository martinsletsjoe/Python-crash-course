file_path = r'C:\Users\M\PycharmProjects\pythonProject10FILESANDEXCEPTIONS\venv\text_files\pi_digits.txt'
# with open(file_path) as file_object:
#     # contents = file_object.read()
#     # print(contents)
#     for line in file_object:
#         print(line.rstrip())

with open(file_path) as file_object:
    lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())
pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))