print("Program starting.")
print("Welcome to the unit converter program!\nFollow the menu instructions below.")

print("\nOptions:")
print("1. - Length\n2. - Weight\n0. - Exit")
choice1 = int(input("Your choice: "))
if choice1 == 1:
    print("\nLength options:")
    print("1. - Meters to kilometers\n2. - Kilometers to meters\n0. - Exit")
    lengthchoice = int(input("Your choice: "))
    if lengthchoice == 1:
        meters1 = float(input("Insert meters: "))
        kilometers1 = meters1 / 1000
        print(f"{meters1} m is {round(kilometers1, 1)} km")
    elif lengthchoice == 2:
        kilometers2 = float(input("Insert kilometers: "))
        meters2 = kilometers2 * 1000
        print(f"{kilometers2} km is {round(meters2, 1)} m")
    elif lengthchoice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice1 == 2:
    print("\nWeight options:")
    print("1. - Grams to pounds\n2. - Pounds to grams\n0. - Exit")
    weightchoice = int(input("Your choice: "))
    if weightchoice == 1:
        grams1 = float(input("Insert grams: "))
        pounds1 = grams1 / 453.59237
        print(f"{grams1} g is {round(pounds1, 4)} lb")
    elif weightchoice == 2:
        pounds2 = float(input("Insert pounds: "))
        grams2 = pounds2 * 453.59237
        print(f"{pounds2} lb is {round(grams2, 1)} g")
    elif weightchoice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice1 == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")