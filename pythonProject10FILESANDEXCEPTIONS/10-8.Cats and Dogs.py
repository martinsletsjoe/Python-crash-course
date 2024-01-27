def print_list_of_names(filename):
    '''Print the contents of all books'''
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    print_list_of_names(filename)

