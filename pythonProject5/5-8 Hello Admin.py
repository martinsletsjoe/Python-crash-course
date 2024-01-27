usernames = ["admin", "user1", "user2", "user3", "user4"]

if not usernames:
    print("empty")
for username in usernames:
    if username == "admin":
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")


    # else:print(f"Hello {username}, thank you for logging in again.")