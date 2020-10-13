# Password-Locker
## Author

[Jeff-Mwai](https://github.com/Jeff-Mwai)

## Description

Password Locker is a python project that enables the user to save their account details and passwords. The platform saves the users details and goes to the extent of generating new passwords.

## User Stories
The user.... :
* Creates an account for the application
* To create an account for the application or log into the application.
* The platform stores the various accounts that the user has.
* Password locker generates a new password for a user that does not have a registered account yet. 
* Password locker enables the user to delete accoun credentials that he or she does no longer require.


## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.6
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/Jeff-Mwai/Password-locker.git```

* cd Password-locker

* code . to open in visual studio code.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ python3 user.py
* To run test for the application
        $ python3 user_test.py

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./python3 user.py```|Hello Welcome to your Accounts Password Store... <br>* CA ---  Create New Account * LI ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```D```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```D```| The application exits|

## Technologies Used

* python3.6

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [mikeycharlesm7@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2019 **Owiti Charles**
