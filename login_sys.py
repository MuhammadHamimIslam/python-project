import getpass

allUserInfo = [
    {
    "username": "Hamim",
    "email": "muhammadhamimislam47@gmail.com",
    "password": "123",
    "user_condition": "Verified"
    },
    {
    "username": "x",
    "email": "mrx@email.com",
    "password": "456",
    "user_condition": "not verified"
    }
]

while True:
    print("Log in: ")
    email = input("Enter the email address: ")
    password = getpass.getpass("Enter the password: ")
    
    for i in allUserInfo: 
        if email in i["email"]: 
            print("User exists")
        
    break