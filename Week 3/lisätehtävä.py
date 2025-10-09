print("Program starting.\nWelcome to the system.")
username = input("Enter your username: ")
user_age = int(input("Enter your age: "))
admin_status = input("Are you an admin? (Y/N): ")

if username == "Matias" and user_age >= 18 and admin_status == "Y":
    print("Accessing admin page")
    print("Options:\n1. Add new user\n2. Check functionality of devices\n0. Exit.")
    choice = int(input("Your choice: "))
    if choice == 1:
        username2 = input("Enter username: ")
        print(f"User {username2} added.")
    elif choice == 2:
        print("All devices are working properly")
    elif choice == 0:
        print("Exiting...")
    else:
        print("Unknown option")
elif username == "Matias" and user_age >= 18:
    print("Accessing user page")
    print("Options:\n1. Check information\n2. Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        print(f"Username is {username} and age is {user_age}.")
    elif choice == 2:
        print("Exiting...")
    else:
        print("Unknown option.")
elif user_age <= 17:
    print("Age is not enough. Access denied.")
elif username != "Matias":
    print("Unauthorized user. Access denied.")
print("Program ending.")