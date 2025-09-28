print("Program starting.")
username = input("This is a program with simple menu, where you can choose which operation the program performs. \nBefore the menu, please insert your name: ")

print("Options")
print("1 - Print welcome message \n0 - Exit")
choice = int(input("Your choice "))

if(choice == 1):
    print("Welcome, ", username, end="!")
elif (choice == 0):
    print("Exiting...")
else:
    print("Unknown option")

print("\nProgram ending.")