print("Welcome to password locker")
print("From the options below, choose lg for login, cr to create a new account and ex for exit")
choice = input()

if choice == "lg":
    print("login")
elif choice == "cr":
    print("create account")
elif choice == "ex":
    exit()
else: 
    print("Invalid. Please try again")