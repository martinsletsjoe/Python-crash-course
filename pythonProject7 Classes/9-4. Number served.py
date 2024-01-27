class Restaurant:
    '''An attempt to model a restaurant.'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize name and cuisine attributes.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Simulate advertising for a restaurant.'''
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        '''Indicate that the restaurant is open.'''
        print(f"{self.restaurant_name} is now open!")

    def served_number(self):
        '''print how many customers have been served.'''
        print(f"{italiensk.restaurant_name} have served {italiensk.number_served} today.")

    def set_number_served(self,number_of_customers):
        '''set the number of customers that have been served.'''
        self.number_served = number_of_customers

    def increment_number_served(self, new_customers):
        '''Add the given amount to the number served'''
        self.number_served += new_customers



husmanskost = Restaurant('Odd', 'Husmanskost')
italiensk = Restaurant('ferruzio', 'antipasti og pølse')

print(f"My restaurants name is {husmanskost.restaurant_name}.")
print(f"We serve {husmanskost.cuisine_type}.")
husmanskost.describe_restaurant()

print(f"\nYour restaurants name is {italiensk.restaurant_name}.")
print(f"your restaurant serves {italiensk.cuisine_type}")
italiensk.open_restaurant()

italiensk.set_number_served(23)
italiensk.served_number()
italiensk.increment_number_served(2)
italiensk.served_number()