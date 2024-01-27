current_users = ["user0", "USER1", "user2", "user3", "user4"]
new_users = ["USER0", "NEW_USER1", "new_user2", "usEr3", "user4"]

a = [x.lower() for x in current_users]
new_userslowers = [z.lower() for z in new_users]


for new_userslower in new_userslowers:
    if new_userslower in a:
        print(f"try another {new_userslower}")
    else:
        print("That username is available")
