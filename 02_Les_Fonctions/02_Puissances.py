#Calcul puissance
def inpA_B(number,puissance):
    if number != int:print("Le nombre | chiffre choisit est inccorect.");return
    Acc = 1
    for i in range(puissance):
        Acc *= number
    print(number,"^",puissance,"=",Acc)

#Récup input
def inp():
    inpA_B(input("Entrée un nombre ou un chiffre : "),input("Entrée une puissance au nombre ou chiffre précédent : "))

inp()