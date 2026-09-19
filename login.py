def login():
    import json

    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("user.json", "r") as file:
        data = json.load(file)

    # find matching user
    user = None
    for u in data["users"]:
        if u["username"] == username and u["password"] == password:
            user = u
            break

    if user is None:
        print("Invalid username or password")
        return

    print(f"\nWelcome back, {username}!\n")