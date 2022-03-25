#Créer une fonction qui calcule la somme des valeurs de toutes les cases d’une liste bidimensionnelle
import random
def define_list():
    def boucle():
        listinp = []
        for i in range(1,11):
            listinp.append(i)
        return listinp
    first_list = []
    index=0
    somme = 0
    for i in range(1,random.randint(1,30)):#Donne random len(first_list)
        first_list.append(boucle())
        somme +=len(first_list[index])
        index +=1

    return somme

print(define_list())