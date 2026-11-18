#Elso feladat

age = int(input("Hany eves vagy? "))

if age >= 18:
    if age < 21:
        print("Adult, but under 21")
    else:
        print("You are 21 or older")
else:
    print("You are under 18")

#Elif hasznalataval
if age < 18:
    print("You are under 18")
elif age < 21:
    print("Adult, but under 21")
else:
    print("You are 21 or older")

#Masodik feladat

username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "python123":
        print ("Login successful!")
    else:
        print("Invalid password.")
else:
    print ("Invalid username")

#Harmadik feladat

score = int(input("Enter your score: "))

if score > 100 or score < 0:
    print("Incorrect score.")
elif score > 89:
    print ("Excellent")
elif score > 69:
    print ("Very good")
elif score > 49:
    print ("Passed")
else:
    print("Failed")