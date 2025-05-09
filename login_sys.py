import getpass
import json

def get_data(): 
    with open('data/user_data.json') as f:
        content = f.read()
    return json.loads(content)



def register(): 
    all_user_info = get_data()
    email = input("Enter the email: ")
    password = getpass.getpass("Enter the password: ")
    for user in all_user_info: 
        if user["email"] != email: 
            #all_user_info.append({"email": email, "password": password})
            with open('data/user_data.json', 'a') as f:
                f.write('{"email": email, "password": password}')
            print("Registration successful")
            return 
    print("User exists")

# login 
def login(): 
    all_user_info = get_data()
    email = input("Enter the email: ")
    password = getpass.getpass("Enter the password: ")
    for user in all_user_info: 
        if user["email"] == email and user["password"] == password: 
            print("Login successful")
            return 
    print("login failed")
    
while True:
    choice = input("Enter your choice: ")
    match choice: 
        case "1": register()
        case "2": login()
        case "3": break
        case _: print("Invalid choice!")