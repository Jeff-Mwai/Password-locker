import random
import string



users = list()
credentials = list()
class Credentials:
    
    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password

    def my_credentials():
        print("Choose one of the following options to continue")
        print("\n1. Create new credentials \n2. Store credentials of existing accounts \n3. View existing credentials \n4. Logout")
        credentials_option = input()
        if credentials_option == "1":
            print("Do you want a system generated password?")
            option = input("\n1. Yes \n2. No")
            if option == "1":
                pwd =Users.random_password(10)
                account1 = Credentials(account_name = input("Account Name (e.g. Twitter): "), username = input("Username: "),  password=pwd)
                credentials.append(account1)
                for x in credentials:
                    print("Account: " + x.account_name,"Username: " + x.username,"Password: " + x.password)
            elif option == "2":
                account1 = Credentials(account_name = input("Account Name (e.g. Twitter): "), username = input("Username: "), password = input("Password: "))
                credentials.append(account1)
                for x in credentials:
                    print("Account: " + x.account_name,"Username: " + x.username,"Password: " + x.password)
            else:
                print("Invalid input")
                Credentials.my_credentials()

        elif credentials_option == "2":
            account1 = Credentials(account_name = input("Account Name (e.g. Twitter): "), username = input("Username: "), password = input("Password: "))
            credentials.append(account1)
            Credentials.my_credentials()
            
        elif credentials_option == "3":
            for x in credentials:
                print("Account: " + x.account_name,"Username: " + x.username,"Password: " + x.password)
        elif credentials_option == "4":
            Users.login()
        else:
            print("Invalid input")



class Users:

    def __init__(self, username, password):

        self.username = username
        self.password = password
        
    def login():
        print("Put your credentials to login")
        username = input("Username: ")
        password = input("Password: ")

        for x in users:
            if x.username == username and x.password == password:
                Credentials.my_credentials()
            else:
                print("Error")
    
    def random_password(length):
    # Random string with the combination of lower and upper case
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

class Main:

    user1 = Users("user", "1234")
    users.append(user1)
    def create_account():
        user1 = Users(input("Username: "), input("Password: "))
        users.append(user1)
        Users.login()


    print("Hello, welcome to Password Locker. Choose one of the three options to continue:")
    print("\n1. Login \n2. Register new account \n3. Exit")
    user_option = input()

    if user_option == "1":
        Users.login()
    elif user_option == "2":
        create_account()
    elif user_option == "3":
        exit()
    else:
        print("Invalid option")



    
