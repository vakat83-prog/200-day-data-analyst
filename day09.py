#Elso feladat

username = input("Adja meg a felhasznalo nevet: ")

print (len(username))
print (username[0])
print (username[-1])

#Masodik feladat

word = input("Kerek egy szot:")

print (word[0])
print (word[1])
print (word[2])
print (len(word))

#Harmadik feladat

username = input("Adja meg a felhasznalo nevet: ")

if len(username) >= 5:
    print ("Username accepted.")
else:
    print("Username too short.")

#Extra

username = input("Adja meg a felhasznalo nevet: ")

print(len(username))
print(username[0])
print(username[-1])

if len(username) >= 5 and len(username) <=10:
    print("Valid username.")
else:
    print("Invalid username.")