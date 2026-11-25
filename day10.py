#Elso feladat
name = input("Enter your full name: ")

name = name.strip()

print(name.lower())
print(name.upper())

#Masodik feladat
car = input("Enter car: ")

new_car = car.replace("Auris", "Corolla")

print(new_car)

#Harmadik feladat

name = input("Enter your full name: ")
new_name = name.split()
print("First name: " + new_name[1])
print("Surname: " + new_name[0])

