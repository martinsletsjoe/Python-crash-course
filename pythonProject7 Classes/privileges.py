'''a simple way to represent an admin'''

from USERS import USER

class Admin(USER):
    '''An attempt to model a admin.'''

    def __init__(self, first_name, last_name, age, sex):
        '''Initialize the admin attributes.'''
        super().__init__(first_name, last_name, age, sex)

        #initialize an empty set of privileges
        self.privileges = Privileges()

class Privileges():
    '''A class to store an admin's privileges'''

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print(f"\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")

# eric = Admin('eric', 'matthes', 22, 'male')
# eric.describe_user()
#
# eric.privileges.show_privileges()
# print(f"\nAdding privileges...")
# eric_privileges = [
#     'can reset passwords',
#     'can moderate discussions',
#     'can suspend accounts',
# ]
# eric.privileges.privileges = eric_privileges
# eric.privileges.show_privileges()