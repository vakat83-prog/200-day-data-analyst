#Elso feladat

age = int(input("Eletkor: "))
experience = int(input("Tapasztalat(ev): "))

if age >= 21 and experience >= 3:
    print("You can apply for a taxi licence.")
else:
    print("You cannot apply for a taxi licence.")

#Masodik feladat

cost = int(input("Kerem a vasarlas osszeget: "))
is_member = input("VIP (Yes/No): ")

if cost >= 100 or is_member == "Yes":
    print("Discount applied.")
else:
    print("No discount available.")

#harmadik feladat

is_blocked = False

if not is_blocked:
    print("Access granted.")
else:
    print("Access denied.")


#Negyedik feladat
age = 25
experience = 4
is_blocked = False

if age >= 21 and experience >= 3 and not is_blocked:
    print("Application approved.")
else:
    print("Application rejected.")