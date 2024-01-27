class USER:
    '''An attempt to model a user'''

    def __init__(self, first_name, last_name, age, sex):
        '''Initialize a user's information'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        '''Summary of the user's information'''
        print(f"\nName is {self.first_name} {self.last_name}, I am a {self.sex}, I am {self.age} years old.")

    def greet_user(self):
        '''personalized greeting to the user'''
        print(f"Hello {self.first_name} {self.last_name}, hope your having a great day.")

# user_one = USER('Kevin', 'Max', 22, 'male')
# user_two = USER('Lisbet', 'Persimmany', 69, 'female')
#
# user_one.describe_user()
# user_one.greet_user()
#
# user_two.describe_user()
# user_two.greet_user()
# print(f"\n{user_two.first_name} is {user_two.age} years old."

class Admin(USER):
    '''An attempt to model a admin.'''

    def __init__(self, first_name = 'admin',last_name ='admin',age='admin',sex='admin'):
        '''Initialize the admin attributes.'''
        super().__init__(first_name, last_name, age, sex)
        self.privileges = []

    def show_privileges(self):
        '''Display the admins privileges.'''
        print(f"\nThis user has these privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin('Admin')
admin.privileges = ['can add post', 'can ban user', 'can noclip pog']

admin.show_privileges()