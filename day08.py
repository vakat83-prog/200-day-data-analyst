#Elso feladat

age = int(input("Kor: "))
experience = int(input("Vezetesi tapasztalat: "))
has_licence = input("Van jogositvany (Yes/No): ")

if age >= 21 and experience >= 3 and has_licence == "Yes":
    print("You meet all taxi driver requirements.")
else:
    print("You do not meet the taxi driver requirements.")

#Masodik feladat

cost = int(input("Vasarlas osszege: "))
is_member = input("VIP tag (Yes/No): ")
coupon = input("Van kupon kodja (Yes/No): ")

if (cost >= 100 and is_member == "Yes") or coupon == "Yes":
    print("Discount applied.")
else:
    print("No discount available.")

#Harmadik feladat

username = "admin"
password = "python123"
is_blocked = False

if username == "admin" and password == "python123" and not is_blocked:
    print("Login successful.")
else:
    print("Access denied.")


