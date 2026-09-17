def register():
    import json

    new_user = {}
    
    new_user["username"] = input("Enter a username: ")
    new_user["password"] = input("Enter a password: ")
    
    if len(new_user["username"])>18:
        print("Username should not be greater than 18 characters")

    elif len(new_user["password"])>8:
        print("Username should not be greater than 8 characters")

    else:
        # read the json file first
        with open("user.json", "r") as file:
            data = json.load(file)
        # now append 
        data["users"].append(new_user)

        # write the list
        with open("user.json", "w") as file:
            json.dump(new_user, file, indent=3)
        
