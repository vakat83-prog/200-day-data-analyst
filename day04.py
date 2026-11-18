#Elso feladat
age = int(input("Add meg az eletkorod: "))

print(f"Felnott: {age >= 18}")

#Masodik feladat

number1 = int(input("Adj meg egy szamot: "))
number2 = int(input("Adj meg egy masik szamot: "))

print(f"Az elso szam nagyobb: {number1 > number2}")
print(f"A ket szam egyenlo: {number1 == number2}")
print(f"Az elso szam kisebb vagy egyenlo a masodiknal: {number1 <= number2}")

#Harmadik feladat

age = int(input("Hany eves vagy? "))

has_license = input("Van ervenyes jogositvanyod? (True/False): ")

license_years = int(input("Hany eve van jogositvanyod? "))

eligible = age >= 21 and has_license == "True" and license_years >= 2

print(f"A feltetelek teljesulnek: {eligible}")

