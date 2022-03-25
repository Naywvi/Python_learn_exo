#Ecrire un programme ayant une variable dont la valeur est à deviner, le programme va demander en boucle 
#une réponse et afficher soit trop haut ou trop bas tant que la valeur rentrée n'est pas la bonne.
import random
print("\nDevine:")
devine_var = random.randint(0,100)
inp = int(input())

while devine_var != inp:
    inp = int(input())
    if inp > devine_var:print("plus bas")
    elif inp < devine_var:print("plus haut")
    else:break
print("Bien joué tu as trouvé:",devine_var,".")