
from privileges import Admin

sven =Admin('sven', 'karlson', 44, 'female')
sven.describe_user()

sven_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can ban leo',
]
sven.privileges.show_privileges()
print(f"\nAdding privileges...")
sven.privileges.privileges = sven_privileges
sven.privileges.show_privileges()