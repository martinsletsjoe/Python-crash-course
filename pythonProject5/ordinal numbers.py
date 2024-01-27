integer_lists = []
for i in range(1,10):
    integer_lists.append(i)
print(integer_lists)
for integer in integer_lists:
    if integer == 1:
        print('1st')
    elif integer == 2:
        print("2nd")
    elif integer == 3:
        print("3rd")
    else:
        print(f"{integer}th")
