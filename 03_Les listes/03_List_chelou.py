#Créer une fonction prenant un entier X en paramètre et créant une liste de X valeurs aléatoires
import random

def chelou(inp):
    listchelou = []
    for i in range(random.randint(0,inp)):
        listchelou.append(i)
    return listchelou
print(chelou(int(input("choisissez un chiffre ou un nombre :"))))