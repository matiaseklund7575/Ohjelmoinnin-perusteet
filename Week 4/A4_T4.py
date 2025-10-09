print("Program starting.")

numberofwords = 0
numberofchars = 0
continueLoop = True

while continueLoop == True:
    word = input("Insert word (empty stops): ")
    numberofwords +=1
    numberofchars +=int(len(word))
    if word == "":
        continueLoop = False

if continueLoop == False:
    print(f"You inserted:\n{numberofwords - 1} words\n{numberofchars} characters")

print("\nProgram ending.")