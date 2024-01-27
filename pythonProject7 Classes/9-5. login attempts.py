class USER:
    '''An attempt to model a user'''

    def __init__(self, first_name, last_name, age, sex):
        '''Initialize a user's information'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        '''Summary of the user's information'''
        print(f"\nName is {self.first_name} {self.last_name}, I am a {self.sex}, I am {self.age} years old.")

    def greet_user(self):
        '''personalized greeting to the user'''
        print(f"Hello {self.first_name} {self.last_name}, hope your having a great day.")

    def increment_login_attempts(self):
        '''increment login attempts'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_one = USER('Kevin', 'Max', 22, 'male')
user_two = USER('Lisbet', 'Persimmany', 69, 'female')

user_one.describe_user()
user_one.greet_user()

user_two.describe_user()
user_two.greet_user()
print(f"\n{user_two.first_name} is {user_two.age} years old.")

user_two.increment_login_attempts()
print(user_two.login_attempts)
user_two.increment_login_attempts()
print(user_two.login_attempts)
user_two.increment_login_attempts()
user_two.increment_login_attempts()
print(user_two.login_attempts)
user_two.reset_login_attempts()
print(user_two.login_attempts)