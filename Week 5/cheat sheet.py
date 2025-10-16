#print() #funktiokutsu
#print("Hello") # "Hello" on funktion parametri
#len()

#while True:
#    print("I can do this forever")

#def greet(name):
#    print(f"Hello {name}")

#print("Here I am")
#name = "Matias"
#greet(name)

#def greet(name):
#    return f"Hello, {name}"

#print(greet("Matias"))

def greeting_airport(person, age):
    print(f"How do you do {person}")
    if age >= 18:
        print("Welcome to your flight")
    else:
        print(f"You need to wait for {18-age} years to fly solo.")

greeting_airport("Matias", 19)