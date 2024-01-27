from random import randint

class Die:
    '''An attempt to model a dice'''
    def __init__(self,sides=6):
        '''Initialize the die attributes.'''
        self.sides = sides

    def roll_die(self):
        return randint(1,self.sides)

    def roll_multiple_times(self,num_rolls=10):
        rolls = []
        for i in range(num_rolls):
            rolls.append(self.roll_die())
        return rolls

six_sided_die = Die()

result = six_sided_die.roll_multiple_times()
print(result)

ten_sided_die = Die(sides=10)
result = ten_sided_die.roll_multiple_times()
print(result)

twenty_sided_die = Die(sides=20)
result = twenty_sided_die.roll_multiple_times()
print(result)






# import random
#
# class Die:
#     def __init__(self, sides=6):
#         self.sides = sides
#
#     def roll(self):
#         return random.randint(1, self.sides)
