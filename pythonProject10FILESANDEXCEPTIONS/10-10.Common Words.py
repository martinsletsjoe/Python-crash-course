def count_words(filename):
    '''Count the number of times a specific word is written.'''
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        word = contents.split()
        num_words = word.count('the ')
        wanted_word = 'the'
        print(f"\nThe book {filename} has the word '{wanted_word}' written in it {num_words} times")
        word = contents.lower().count('the ')
        print(f"The book {filename} has the word '{wanted_word}' written in it {word} times")
        word = contents.count('the')
        print(f"The book {filename} has the word '{wanted_word}' written in it {word} times")
        word = contents.lower().count('the')
        print(f"The book {filename} has the word '{wanted_word}' written in it {word} times")

filenames = ['The Analysis of Mind.txt', 'The Principles of Psychology, Volume 1 of 2.txt',  'The Science of Human Nature.txt']
for filename in filenames:
    count_words(filename)