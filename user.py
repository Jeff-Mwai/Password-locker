users = list()

class Users:

    def __init__(self, username, password):

        self.username = username
        self.password = password
        
    def login():
        print("Put your credentials to login")
        username = input("Username: ")
        password = input("Password: ")
        user1 = users(username, password)
        if username ==user1.username and password == user1.password:
            print("Login successful")
        else:
            print("Error")

class Main:

    def create_account():
        user1 = Users(input("Username: "), input("Password: "))
        users.append(user1)
        Users.login()
        
        for x in users:
            print(x.username)
        

   



    print("Hello, welcome to Password Locker. Choose one of the three options to continue:")
    print("\n1. Login \n2. Register new account \n3. Exit")
    user_option = input()

    if user_option == "1":
        login()
    elif user_option == "2":
        create_account()
    elif user_option == "3":
        exit()
    else:
        print("Invalid option")

    
