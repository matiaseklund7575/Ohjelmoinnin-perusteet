print(f"Program starting.")

compound = input("\nInsert a closed compound word: ")

print(f"The word you inserted is \'{compound}\' and in reverse it is \'{compound[::-1]}\'")
print(f"\nThe inserted word length is {len(compound)}")
print(f"Last character is \'{compound[-1]}\'")

print("\nTake substring from the inserted word by inserting...")
value1 = int(input("1) Starting point: "))
value2 = int(input("2) Ending point: "))
value3 = int(input("3) Step size: "))


print(f"\nThe word \'{compound}\' sliced to the defined substring is \'{compound[value1:value2:value3]}\'")
print("\nProgram ending.")




#print("Program starting.")
#
#compound = input("\nInsert a closed compound word: ")

#print("The word you inserted is ", compound, " and in reverse it is ", compound[::-1], sep="'", end="'.")
#print("\nThe inserted word length is", len(compound))
#print("Last character is ", compound[-1], sep="'", end="'.")

#print("\n\nTake substring from the inserted word by inserting...")
#value1 = int(input("1) Starting point: "))
#value2 = int(input("2) Ending point: "))
#value3 = int(input("3) Step size: "))


#print("\nThe word ", compound, " sliced to the defined substring is ", compound[value1:value2:value3], sep="'", end="'.")
#print("\nProgram ending.")