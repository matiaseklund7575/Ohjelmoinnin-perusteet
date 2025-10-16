print("Program starting.")


stepcount = 0
startingValue = int(input("Insert a positive integer: "))

i=startingValue

while i > 1:
    print(f"{int(i)} -> ", end="")
    if i % 2 == 0:
        i/=2
    else:
        i*=3
        i+=1
    stepcount+=1
print("1")

print(f"Sequence had a total of {stepcount} steps.")

print("\nProgram ending.")