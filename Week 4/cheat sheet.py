children = 0
hometown = "Hämeenlinna"

Townsinfinland = ["Lahti", "Helsinki", "Hämeenlinna", "Oulu", "Tampere"]

Randominformation = ["Matias", 19, True, children, hometown]

#print(Townsinfinland[0])
#Townsinfinland.append("Rovaniemi")
#print(Townsinfinland)

Numoftowns = len(Townsinfinland)#
#print(Townsinfinland[Numoftowns-1])

Municipalities = ["Hattula", "Janakkala", "Kangasala", "Forssa"]
Towns = ["Lahti", "Helsinki", "Hämeenlinna", "Oulu", "Tampere"]

MunicipalitiesandTowns = [Municipalities, Towns]

#print(MunicipalitiesandTowns[1][-2])

#Towns.sort()
#print(Towns)

Teacher = {
    'name': 'Juha',
    'age': 50,
    'city': 'Lahti'
}

#print(Teacher["name"])

#Teacher['email'] = 'juha.hyytiainen@lab.fi'

#print(Teacher)

#for key in Teacher:
#    print(key, end=' ')
#    print(Teacher[key])

Student = [
    {'name': 'Mikko', 'age': 25, 'city': 'Tampere'},
    {'name': 'Maija', 'age': 29, 'city': 'Espoo'},
    {'name': 'Seppo', 'age': 45, 'city': 'Helsinki'},
]

#print(Student[0])

Cities = {
    'Finland':['Tampere', 'Espoo', 'Helsinki'],
    'Sweden':['Stockholm', 'Malmö']
}

#print(Cities['Finland'][0])

#for town in Towns:
#    print(f"The town of {town}")
#print(f"All the towns {Towns}")

#for i in range(1, 10):
#    print(i)

#for i in range(1, 10):
#    print(i, end=' ')

for i in range(1, 10, 3):
   print(i)

#Total = 0
#for i in range(1,101):
#    Total +=i
#    print(Total)

#print(Total)

#for i in range(9):
#    if (i == 3):
#        continue
#    print(i)

#for i in range(10):
#    if (i == 5):
#        break
#    print(i)

#i = 0
#while i < 10:
#    print(f"Iteration number: {i}")
#    i += 1

#continueLoop = True
#while continueLoop == True:
# #   if input("Do you want to continue ") != "yes":
#        continueLoop = False

#while True:
#    if input("Do you want to continue? ") != "yes":
#        break
#    else:
#        continue