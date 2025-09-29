print("Program starting.")

print("\nOptions:")
print("1. - Celsius to fahrenheit\n2. - Fahrenheit to Celsius\n0. - Exit")
choice = int(input("Your choice: "))
if choice == 1:
    celsius1 = float(input("Insert the amount of celsius: "))
    fahrenheit1 = celsius1 * 1.8 + 32
    print(f"{celsius1} °C equals to {round(fahrenheit1, 1)} °F")
elif choice == 2:
    fahrenheit2 = float(input("Insert the amount of Fahrenheit: "))
    celsius2 = (fahrenheit2 - 32) / 1.8
    print(f"{fahrenheit2} °F equals to {round(celsius2, 1)} °C")
elif choice == 0:
    print("Exiting...")
else:
    print("Invalid choice")

print("\nProgram ending")