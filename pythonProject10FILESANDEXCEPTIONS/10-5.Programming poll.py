filename = 'programming poll.txt'

yeet = ''
while yeet == '':
    yeet = input('What part of programming do you like the most?\n ')
with open(filename, 'a') as file_object:
    file_object.write(yeet)


