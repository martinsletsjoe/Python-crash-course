favourite_numbers = {
    "lars": [6, 1, 100],
    "oskar": [420, 1337, 89, 666],
    "johan": [69, 2, 17, 54, 13],
    "leo": [4, 22, ],
    "chris": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, ],
}

for name, number in favourite_numbers.items():
    print(f"\n{name.title()} favourite numbers are: {number}")
    for numbers in number:
        print(f"\t{numbers}")