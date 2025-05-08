import getpass

all_user_info = users = [
    {"email": "a@email.com", "password": "pass1"},
    {"email": "b@email.com", "password": "pass2"},
    {"email": "c@email.com", "password": "pass3"},
    {"email": "d@email.com", "password": "pass4"},
    {"email": "e@email.com", "password": "pass5"},
]

def register(): 
    email = input("Enter the email: ")
    password = getpass.getpass("Enter the password: ")
    for user in all_user_info: 
        if user["email"] != email: 
            all_user_info.append({"email": email, "password": password})
            print("Registration successful")
            return 
    print("User exists")

# login 
def login(): 
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