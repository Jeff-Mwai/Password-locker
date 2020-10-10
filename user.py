users = []

class Users:

    def __init__(self, username, password):

        self.username = username
        self.password = password





class Main:

    def __init__(self, username,password):

        self.username = username
        self.password = password

    def create_account():
        user1 = Users(input("Username: "), input("Password: "))
        


    print("Hello, welcome to Password Locker. Choose one of the three options to continue:")
    print("\n1. Login \n2. Register new account \n3. Exit")
    user_option = input()

    if user_option == "1":
        print("Login")
    elif user_option == "2":
        create_account()
    elif user_option == "3":
        exit()
    else:
        print("Invalid option")

    
