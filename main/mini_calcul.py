def message_accueil():
    print("bienvenue sur la mini-calculatrice")
  
def saisir_nombre():
  num1 = float(input("entrez le premier nombre: "))
  num2 = float(input("entrez le deuxieme nombre: "))
  return num1, num2
  
def menu ():
  print("===Menu===")
  print("1. Addition")
  print("2. Soustraction")
  print("3. multiplication")
  print("4. division")
  
  choix= input("entrez votre choix (1-4): ")
  while choix not in ["1", "2", "3", "4"]:
        choix = input("Choix invalide. Entrez votre choix (1-4) : ")
  return choix   

def sum(a, b):
  return a + b

def substraction(a, b):
  return a - b

def multiplication(a, b):
  return a * b

def division(a, b):
  if b !=0:
    return a / b
  else:
    print("Erreur: division par zéro")
    
def run_calcul(choix):
  num1, num2 = saisir_nombre()
  match choix:
    case '1':
        result = sum(num1, num2)
    case '2':
        result = substraction(num1, num2)
    case '3':
        result = multiplication(num1, num2)
    case '4':
        result = division(num1, num2)
    case _:
        print("Choix invalide.")
  return result

if __name__== "__main__":
    message_accueil()
    choix= menu()
    result = run_calcul(choix)
    if result is not None:
     print("le résultat est : {result}")

