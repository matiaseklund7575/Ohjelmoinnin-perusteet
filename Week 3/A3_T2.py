print("Program starting.")
print("String comparisons")
word1 = input("Insert first word ")
char = input("Insert character ")

if(char in word1):
    print("Word ", word1, " contains character ", char, sep='"', end='"')
else:
    print("Word ", word1, " doesn't contain character ", char, sep='"', end='"')

word2 = input("\nInsert second word ")




if(word1 < word2):
    print("The first word ", word1, " is before the second word ", word2, " alphabetically.", sep='"')
elif(word2 < word1):
    print("The second word ", word2, " is before the first word ", word1, " alphabetically", sep='"')
else:
    print("The words are the same alphabetically ", word1, sep='"', end='".')