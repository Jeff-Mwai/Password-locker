import random
import string



users = list()
credentials = list()

"""
declared two empty lists to store data
"""

class Credentials:
    
    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password

        """
        Created the class credentials and initialized using the self keyword
        """

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
                Users.view_credentials()
                Users.delete()
                # for x in credentials:
                #     print("Account: " + x.account_name,"Username: " + x.username,"Password: " + x.password)
            elif option == "2":
                account1 = Credentials(account_name = input("Account Name (e.g. Twitter): "), username = input("Username: "), password = input("Password: "))
                credentials.append(account1)
                # for x in credentials:
                #     print("Account: " + x.account_name,"Username: " + x.username,"Password: " + x.password)
                Users.view_credentials()
                Users.delete()
            else:
                print("Invalid input")
                Credentials.my_credentials()

        elif credentials_option == "2":
            account1 = Credentials(account_name = input("Account Name (e.g. Twitter): "), username = input("Username: "), password = input("Password: "))
            credentials.append(account1)
            Users.view_credentials()
            Users.delete()                  
            
        elif credentials_option == "3":
            Users.view_credentials()
            # for x in credentials:
            #     print("Account: " + x.account_name,"Username: " + x.username,"Password: " + x.password)
        elif credentials_option == "4":
            print("You have logged out")
            exit()
        else:
            print("Invalid input")
            Credentials.my_credentials()

        """
        The credentials class has methods that are used to either input details of existing accounts, generate password and view the stored credentials
        """



class Users:

    def __init__(self, username, password):

        self.username = username
        self.password = password

        """
        Created class users and initialized using the self keyword
        """
        
    def login():
        print("Put your credentials to login")
        username = input("Username: ")
        password = input("Password: ")

        for x in users:
            if x.username == username and x.password == password:
                print("Login successful")
                Credentials.my_credentials()
            else:
                print("Error")
                

        """
        Created a login method that authenticates the users' details
        """

    def view_credentials():
        print("You can choose one of the options below to view your credentials:")
        print("\n1. Yes \n2. No")
        viewers_choice = input()
        if viewers_choice == "1":
            for x in credentials:
                print("Account: " + x.account_name,"Username: " + x.username,"Password: " + x.password)
        elif viewers_choice == "2":
            print("Thanks for visiting")
            Users.login()
        else:
            print("invalid choice")
            Users.login()

    def delete():
        print("Do you want to delete credentials that you no longer want in the application?")
        print("\n1. Yes \n2. No")
        delete_option = input()
        if delete_option == "1":
            credentials.clear()
            print("You have deleted credentials from the list")
        elif delete_option == "2":
            print("your details are still stored in the application")
        else:
            print("Invalid input.")
            delete()



    
    def random_password(length):
    # Random string with the combination of lower and upper case
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    """
    created a method to generate a random password
    """

class Main:

    user1 = Users("user", "1234")
    users.append(user1)
    def create_account():
        user1 = Users(input("Username: "), input("Password: "))
        users.append(user1)
        Users.login()

    """
    Created a create account method that calls the login functiong
    """
    def main():

        print("Hello, welcome to Password Locker. Choose one of the three options to continue:")
        print("\n1. Login \n2. Register new account \n3. Exit")
        user_option = input()

        if user_option == "1":
            Users.login()
        elif user_option == "2":
            Main.create_account()
        elif user_option == "3":
            exit()
        else:
            print("Invalid option")

if __name__ == '__main__':
    Main.main()

    
