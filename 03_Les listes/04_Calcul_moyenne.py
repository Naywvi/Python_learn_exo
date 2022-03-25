#Créer une fonction calculant la moyenne des valeurs d'une liste remplit de chiffres
#Moyenne = Somme des valeurs / effectif total
import random

def moyenne_random():
    slice = [];somme = 0
    for i in range(random.randint(0,50)):
        slice.append(i)
        somme += i
    return somme/len(slice)
print(moyenne_random())