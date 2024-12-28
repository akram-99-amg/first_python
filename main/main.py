print("hello, world")
print (17+35*2)

nom = "Mazegh"
prénom = "Akram"
age = 22
print(f" boujour je m'appelle {prénom} {nom} et j'ai {age} ans.")
print(" Boujour je m'appelle " + prénom + " " + nom + " et j'ai " + str(age) + " age" )


est_etudiant = True
print(type(est_etudiant))
print(type(age))

dragon_ball =["goku", "vegeta", "gohan", "trunks"]
dragon_ball[3]="goten"
dragon_ball.append("trunks")
dragon_ball.sort()
print(dragon_ball)

nbr =[1,2,5,6,"ak"]
print ("ak" in nbr)

fruits = ["pomme","banane", "orange"]
fruits.append ("kiwi")
print(fruits)

del fruits[2]
print(fruits)

print(len(fruits))

fruits.sort()
print(fruits)
