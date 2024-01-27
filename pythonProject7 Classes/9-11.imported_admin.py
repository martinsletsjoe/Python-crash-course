from USERS import USER, Admin, Privileges

karl = Admin('karl', 'fon', 33, 'male')
karl.describe_user()

karl.privileges.show_privileges()
print(f"\nAdding privileges")
karl_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
karl.privileges.privileges=karl_privileges
karl.privileges.show_privileges()