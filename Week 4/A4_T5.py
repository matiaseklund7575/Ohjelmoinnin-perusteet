print("Program starting.")

value1 = int(input("\nInsert starting point: "))
value2 = int(input("Insert stopping point: "))
value3 = int(input("Insert inspection point: "))

print() #tyhjä rivi

if value2 < value1:
    print("Starting point value must be less than the stopping point value.")
if value3 > value2 or value3 < value1:
    print("Inspection value must be within the range of start and stop.")
else:
    print("First loop - inspection with break:")
    for i in range(value1, (value2+1)):
        if i == value3:
            break
        else:
            print(i, end=" ")
        
    print("\nSecond loop - inspection with continue:")
    for i in range(value1, (value2+1)):
         if i == value3:
            continue
         else:
            print(i, end=" ")
       

print("\n\nProgram ending.")