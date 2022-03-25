#Créer un dictionnaire stockant des personnes via leur nom (en clef) et leur age (en valeur)
import random
dictionnaire = {}
list_prenom = ["Nagib", "Pierre","Yacine","Jean"]

for i in list_prenom:
    age = random.randint(5,80)
    dictionnaire[i] = age#[i] pour selectionner l'id soit le prenom donc la cle

for cle_prenom,valeur_age in dictionnaire.items():#.items() similaire au bufio scanner
    print(cle_prenom,"a",valeur_age,"ans.")
