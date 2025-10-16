def menu():
    print("Options: ")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
    return None

def getChoice():
    choice = int(input("Your choice: "))
    return choice

def main():
    print("Program starting.")
    print()
    word = ""
    choice = -1
    while choice != 0:
        menu()
        choice = getChoice()
        if choice == 1:
            word = input("Insert word: ")
        elif choice == 2:
            print(f"Current word - \"{word}\"")
        elif choice == 3:
            print(f"Word reversed - \"{word[::-1]}\"")
        elif choice == 0:
            print("Exiting program.")   
        else:
            print("Unknown option")
    print()
    print("Program ending.")

main()