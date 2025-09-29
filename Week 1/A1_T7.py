print("Calculate fuel consumption.")
distance = int(input("Enter travel distance(kilometers): "))
usage = int(input("Enter fuel usage(liters): "))
consumption = (usage / distance) * 100
print(f"Fuel consumption is {round(consumption)} l per 100 km")