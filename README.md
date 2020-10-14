# Password_Locker

#### Author: [Ronald Kiprotich](https://github.com/RonaldKiprotich)

## Description

This project is a python application that manages our passwords and even generate new passwords for us.


## User Stories
The user would like to.... :
* Create an account for the application.
* Store my existing acounts login details for various accounts that i have registered for.
* Generate new password for an account that i haven't registered for and store it with the account name.   
* Delete stored account login details that i do now want anymore.



## Features


As a user of the terminal application you will be able to:

1. Create an account for the application
2. Log into your account
3. Add credentials for different accounts
4. Store and generate passwords
6. Search for a saved credential
8. Delete a saved credential


Link:-> ```https://github.com/RonaldKiprotich/Password-Locker.git```

2. Clone the project.

3. Get into Python folder (cd into Python).

4. If you have all the Pre-requisites you can run the application.

### Pre-requisites

**What you need to install the application and how to install them.**

```
Python3.8
```

To Install **python 3.8** on terminal execute

```
apt-get install python3.6
```

```
apt-get install pip3
```

## Running the application

1. Navigate into the cloned folder using terminal and enter command `password.py` to run the app.
The app will open on terminal 

2. Follow and answer the prompts to use the application.

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ password.py```|Hello Welcome to your Password Locker... <br>* cr ---  Create New Account *  |
|Select  cr| input username and password.cr----to type your own password,sg----system generated password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select lg  | Enter your password and username you signed up with|  menu to help you navigate through the application|
|Store a new credential in the application| Enter ```nc```|Enter Account's name, Accounts' username, Account's password<br>choose ```en``` to enter your password or ```sg``` for the application to generate a password for you |
|Display all stored credentials | Enter ```dc```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Search a stored credential based on account name|Enter ```dc```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```dl```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exist|
|Exit the application| Enter ```ex```| The application bids you goodbye and exits|

## Built With

* [Python3.8](https://docs.python.org/3/)


### License

* LICENSED UNDER   MIT LICENSE