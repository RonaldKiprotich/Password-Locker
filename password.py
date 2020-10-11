persons = []


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register():
        person1 = User(input("Your Username: "), input("Your Password: "))












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



