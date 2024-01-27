prompt = "vælkommen til tonjes tshortær"
print(prompt)

def make_shirt(size = 'Large', text_of_message = 'I love python'):
    '''Display information about t-shirt options'''
    print(f"\nI would like a {size} t-shirt, with '{text_of_message} written on it.'")

make_shirt('large', 'pogchamperu')
make_shirt(size='medium', text_of_message='not pogchamp')
make_shirt()