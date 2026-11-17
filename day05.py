#Elso feladat

income = float(input("Add meg a napi beveteled: "))

if income >= 200:
    print("Kiváló nap!")
elif income >= 150:
    print("Jó nap!")
elif income >= 100:
    print("Átlagos nap.")
else:
    print("Gyenge nap.")

#Masodik feladat

age = int(input("Hany eves vagy? "))

has_license = input("Van ervenyes jogositvanyod? (True/False): ")

license_years = int(input("Hany eve van jogositvanyod? "))

if age >= 21 and has_license == "True" and license_years >= 2:
    print("Megfelel a felteteleknek!")
else:
    print("Nem felel meg a felteteleknek!")