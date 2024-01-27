new_users = ["USER0", "NEW_USER1", "new_user2", "usEr3", "user4"]
new_userslowers = []
for user in new_users:
  user_to_lowercase = user.lower()
  # med += syntax
  new_userslowers += user_to_lowercase
  # mew list append metode
  new_userslowers.append(user_to_lowercase)

print(new_userslowers)