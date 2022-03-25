#Créer une fonction créant 2 listes de valeurs aléatoires et qui donne en 
#résultat une nouvelle liste qui est la concaténation des deux premieres.

import random

def moyenne_random(index):
    slice1 = ["FIRST"];slice2 = ["SECOND"]

    def boucle():
        listindex = []
        for i in range(random.randint(0,10)):
            listindex.append(i)
        return listindex

    slice1 += boucle();slice2 += boucle()#+= pour pouvoir garder les paramètres de départ, mais peut être retiré

    result = slice1 + slice2
    return result

print(moyenne_random(2))