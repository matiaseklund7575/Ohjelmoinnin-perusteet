def askName():
    userInput = input("Insert name: ")
    return userInput

def greetUser(PName):
    print(f"Hello {PName}!")
    return None

def main():
    print("Program starting.")
    name = askName()
    greetUser(name)
    print("Program ending.")
    return None

main()