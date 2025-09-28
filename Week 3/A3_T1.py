print("Program starting.")
print("insert 2 integers")
num1 = int(input("Insert integer "))
num2 = int(input("Insert second integer "))

print("Comparing inserted integers")

if (num1 > num2):
    print("first integer is larger")
elif(num2 > num1):
    print("second integer is larger")
else:
    print("The integers are the same")

sum = num1 + num2
remainder = sum % 2

print("\nAdding integers together")
print(num1, "+", num2, "=", sum )

print("\nchecking parity of the sum")

if(remainder == 0):
    print("The sum is even")
else:
    print("The sum is odd")

print("Program ending.")