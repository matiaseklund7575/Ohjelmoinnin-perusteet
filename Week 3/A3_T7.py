print("Program starting.")
print("Testing decision structures.")
integer = int(input("Insert an integer: "))

print("Options:\n1 - In one multi-branched decision\n2 - In multiple independent if-statements\n0 - Exit")
choice = int(input("Your choice: "))

if choice == 1:
    print("Using one multi-branched decision structure.")
    if integer >= 400:
        integer += 44
    elif integer >= 200:
        integer += 22
    elif integer >= 100:
        integer += 11
    print(f"Result is {integer}")
elif choice == 2:
    print("Using multiple independent if-statements structure.")
    if integer >= 400:
        integer += 44
    if integer >= 200:
        integer += 22
    if integer >= 100:
        integer += 11
    print(f"Result is {integer}")
elif choice == 0:
    print("Exiting...")
else: 
    print("Unknown option.")

print("Program ending.")