#Créer une fonction prenant un entier et une liste en paramètre et qui affiche si oui ou non cet entier est présent dans cette liste
import random

def Is_in_theList(entier):
    listIn = []
    for i in range(0,50,random.randint(1,9)):
        listIn.append(i)

    for i in listIn:
        if i == entier:return "yes"
        
    return "no, sad try again."


print(Is_in_theList(int(input("Write a number between 0 - 50 : "))))