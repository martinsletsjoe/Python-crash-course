class Restaurant:
    '''An attempt to model a restaurant.'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize name and cuisine attributes.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''Simulate advertising for a restaurant.'''
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        '''Indicate that the restaurant is open.'''
        print(f"{self.restaurant_name} is now open!")

# husmanskost = Restaurant('Odd', 'Husmanskost')
# italiensk = Restaurant('ferruzio', 'antipasti og pølse')
#
# print(f"My restaurants name is {husmanskost.restaurant_name}.")
# print(f"We serve {husmanskost.cuisine_type}.")
# husmanskost.describe_restaurant()
#
# print(f"\nYour restaurants name is {italiensk.restaurant_name}.")
# print(f"your restaurant serves {italiensk.cuisine_type}")
# italiensk.open_restaurant()