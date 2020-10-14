
import random
import string

persons = list()
cred_list = []

class User:
    def register():
        person1 = User(input("Your Username: "), input("Your Password: "))
        persons.append(person1)
        print("Credentials created successfully")
        User.login()

 
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login():
        print("Put in your details to login")
        username1 = input("Username: ")
        password1 = input("Password: ")
        print("Logged in successfully")
        Cred.saveCredential()

class Cred:
    def __init__ (self,accountname,username,password):
        self.accountname = accountname
        self.username = username
        self.password = password

    def passwordGenerate(stringLength=8):
        """
        method that generate a random password
        """
        password = string.ascii_lowercase + string.ascii_uppercase + "~!@#$%;:^&*"
        return ''.join(random.choice(password) for i in range(int(stringLength)))    

    def saveCredential():
        print ("To proceed choose the following. Choose the shortcodes: \n sc- Save Credential\n fc - Find Credentials\n dc- Display credential\n dl- delete credential\n ex- exit\n") 
        option = input().lower()

        if option == 'sc':
            print("Enter your Accounts credentials:\n")
            print("Account name:")
            account_name = input()
            print("Username:")
            user_name = input()
            print("Will you like to en - enter your password or sg - system generated?")
            passwordChoice = input()
            if passwordChoice == 'en':
                print("please input your password")
                pass_word = input()
                # new_cred = Credential()
                # Cred.saveCredential()
                cred1 = Cred(account_name, user_name, pass_word)
                cred_list.append(cred1)
                print("Your account has been created Successfully")
                # Cred.saveCredential()
            elif passwordChoice == 'sg':
                pass_word = Cred.passwordGenerate(8)
                print(f"Your password is: {pass_word}")
                # cred1 = Cred(input("Accountname: "), input("Username: "))
                # cred_list.append(cred1)
                # print(cred1.accountname, cred1.username, cred1.password)
                cred1 = Cred(account_name, user_name, pass_word)
                cred_list.append(cred1)
                print("Your account has been created successfully")
                # Cred.saveCredential()
            else:
                print("invalid choice")
            Cred.saveCredential()
            
            
                 
        elif option == 'fc':
            print("Account name you will like to find?")
            accountname = input()
            if (len(cred_list)>0):
                for credential in cred_list:
                    if credential.accountname == accountname:
                        print(f"Account name: {credential.accountname} Username : {credential.username} Password : {credential.password}")
                    else:
                        print("Account name does not exist") 
            else:
                print("Account name does not exist") 

                Cred.saveCredential()

        elif option == 'dc':
            print("display credentials")
            if (len(cred_list)>0):
                for credential in cred_list:
                    accountname = credential.accountname
                    username = credential.username
                    password = credential.password
                    print(f"Account name : {accountname}\n Password: {password}\n Username : {username}")
            else:
                print("you have no credentials saved.")
            Cred.saveCredential()

        elif option == 'dl':
            print("Enter account name you will like to delete")
            accountname = input()
            for credential in cred_list:
                if credential.accountname == accountname:
                    cred_list.remove(credential)
            print("account deleted successfully")  
            Cred.saveCredential()      

        elif option == 'ex':
            print("Bye")

        else:
            print("Invalid option")    


if __name__ == '__main__':

    print("Welcome to password locker")
    print("From the options below, choose lg - login or cr - create a new account and ex for exit")
    choice = input()

    if choice == "lg":
        print("login")
    elif choice == "cr":
        User.register()
    elif choice == "ex":
        exit()
    else: 
        print("Invalid. Please try again")



