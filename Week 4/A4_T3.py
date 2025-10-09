print("Program starting.")

value1 = int(input("\nInsert starting value: "))
value2 = int(input("Insert stopping value: "))

print("\nStarting while-loop:")

i = value1
while i < (value2+1):
    print(i, end=" ")
    i+=1

print("\nProgram ending.")