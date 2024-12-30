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


info = { "poids" : "16 kg", "origine": "maroc"
    
}
info["nom"] ="labradore"
contact = []
contact.append(info)
print(contact)

ensoleille = True
if ensoleille:
    print("on va à la plage")
else:
    print("on reste à la maison")
    
avec_soleil = True
en_semaine = False
if avec_soleil and not en_semaine:
    print("on va à la plage !")
elif avec_soleil and en_semaine:
    print("on va au travail !")
else:
    print("on reste à la maison !")
    
ensoleille = False
neige = True
if ensoleille:
    print("on va à la plage !")
elif neige:
    print("on fait un bonhomme de neige")
else:
    print("on reste à la maison !")
    

#persopref = "gohan"
#match persopref:
    #case "goku":
     #   print("ce n'est pas lui")
    #case "vegeta":
    #    print("non")
    #case "gohan":
    #    print("c'est lui")
    #case _:
    #    print("aucun de ces perso")    
        
naruto =["kakashi","itachi","sasuke","pain"]
for ninja in range(2,5):
    print(naruto)
        
        
for i in range(10):
    if i == 5:
        break
    print(i)
    
    
for i in range(10):
    if i == 5:
        continue
    print(i)
    
def message ():
    print("hello world")
message()

def addition (a, b):
    resultat= a + b
    return resultat, a, b

retour=addition(20, 20) 
print(retour)
   


#nom= input("entrer un nom :")
#prénom=input("entrer un prénom :")

#resultat= nom + prénom
#print(f"votre nom complet est : {resultat}")

numerateur= input("entrez le numerateur :")
denominateur= input("entrez un denominateur :")
try:
    resultat= int(numerateur) / int(denominateur)
    print(f"votre résultat est {resultat}")
except ValueError:
    print("Erreur :essayez un nombre")
except ZeroDivisionError:
    print("Erreur :devision par 0")