
import random

persons = list()
cred_list = []

class User:
    def register():
        person1 = User(input("Your Username: "), input("Your Password: "))
        persons.append(person1)
        User.login()

 
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login():
        print("Put in your details to login")
        username1 = input("Username: ")
        password1 = input("Password: ")
        #person_combined = username + password
        # for obj in persons:
        #     print()
        # if username1 == person1.username and password1 == person1.password:
        #     print("almost there")
        # else:
        #     print("matata")
        Cred.saveCredential()

class Cred():
    def __init__ (self,accountname,username,password):
        self.accountname = accountname
        self.username = username
        self.password = password

    def saveCredential():
        print ("To proceed choose the following. Choose the shortcodes: \n sc- Save Credential\n fc - View Credentials\n dc- Display credential dl- delete credential ex- exit\n") 
        option = input().lower()

        if option == 'sc':
            Print("Enter your Accounts credentials:\n")
            print("Account name:")
            accountname = input()
            print("Username:")
            username = input()
            print("Will you like to en - enter your password or sg - system generated?")
            passwordChoice = input.lower()
            if passwordChoice == 'en':
                password = input()
            if passwordChoice == 'sg':
                pass
                
            cred_list.append(accountname,username,password)     
     
            
        elif option == 'fc':
            print("Account name you will like to find?")
            accountname = input()
            for credential in cred_list:
                if credential.accountname = accountname:
                    print(credential)
        
        elif option == 'dc':
            print("display credentials")
            if (len(cred_list)>0):
                for credential in cred_list:
                    accountname = credential.accountname
                    username = credential.password
                    password = credential.password
                    print(f"Account name : {accountname}\n Password: {password}\n Username : {username}")

        elif option == 'dl':
            print("Enter account name you will like to delete")
            accountname = input()
            for credential in cred_list:
                if credential.accountname = accountname:
                    cred_list.remove(credential)
            print("account deleted successfully")        

        elif option == 'ex':
            print("Bye")

        else:
            print("Invalid option")    

    def generate_random_password():

              


print("Welcome to password locker")
print("From the options below, choose lg for login, cr to create a new account and ex for exit")
choice = input()

if choice == "lg":
    print("login")
elif choice == "cr":
    User.register()
elif choice == "ex":
    exit()
else: 
    print("Invalid. Please try again")



