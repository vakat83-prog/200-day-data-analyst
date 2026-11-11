#Elso feladat
a = 25
b = 7

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#Masodik feladat
number = int(input("Enter a number: "))

print(number % 2 == 0)

#Harmadik feldat
weight = float(input("Mi a sulyod: "))
target_weight = float(input("Mi a celod: "))

weight_loss = weight - target_weight

print(f"{weight_loss} kg-ot kell meg leadnod.")

#Negyedik feladat - Taxi bevételkalkulátor

kilometers = float(input("Megtett kilometerek: "))

price_per_km = float(input("Egy kilometere juto dij: "))

base_fee = float(input("Alapdij: "))

total_fare = kilometers * price_per_km + base_fee

print(f"A teljes viteldij: £{total_fare}")
