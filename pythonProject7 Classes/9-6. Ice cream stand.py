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

class IceCreamStand(Restaurant):
    '''A simple attempt to model an Ice Cream stand.'''

    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        '''Initialize the icecreamstands attributes.'''
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_IceCream_flavors(self):
        '''Display the flavors available.'''
        print(f"\nWe have all these flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'strawberry']

big_one.describe_restaurant()
big_one.show_IceCream_flavors()