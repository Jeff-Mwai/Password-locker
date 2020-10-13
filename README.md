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
|Open the application on the terminal | Run the command ```$ ./python3 user.py```|Hello, welcome to Password Locker. Choose one of the ... <br>*
|Select  2| input username and password| Your account has been created successfully.`|
|Select 1  | Put your credentials to login| There are choices to help the user in moving from one step to the other|
|Select 1  | Create new credentials| Choose to enter own password or system generated password|
|Select 2  |  Store credentials of existing accounts| Options provided to input accountname, username and password|
|Select 3  |  View existing credentials| The already inputed account details of the user can be viewed|

## Technologies Used

* python3.6

## Known Bugs
* There are no known bugs at the moment

## Contact Information 

If you have any question or contributions, please email me at [jeffmwai3@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2019 **Owiti Charles**
