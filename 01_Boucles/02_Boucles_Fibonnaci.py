#Ecrire un programme qui calcule la 20eme valeur de la suite de Fibonacci.
from pickle import APPEND


Acc = 1
AccTwo = 1
for i in range(2,21,1):
    result = Acc + AccTwo
    Acc = AccTwo
    AccTwo = result
print(result)

#Récursive
def fibo(nb):
    if nb <=1:
        return nb
    return fibo(nb-1) + fibo(nb-2)

#Récursive Opti
L = {0:0,1:1}
def fibo(nb):
    if nb in L:
        return L[nb]
    L[nb]=fibo(nb-1) + fibo(nb-2)
    return fibo(nb-1) + fibo(nb-2)