#Créer une fonction permettant de connaitre le nombre de personnes majeures dans le le dictionnaire.
import random

def old():
    #Création du dictionnaire et attribution des prénoms
    dictionnaire_de_famille = {}
    list_prenom = ["Nagib", "Pierre","Yacine","Jean","Mathilde","Le moche"]
    list_age = []

    #attribution de l'âge
    for i in list_prenom:
        age = random.randint(1,90)
        list_age.append(age)#récupération moche de l'âge dans une list
        dictionnaire_de_famille[i] = age

    #Récupération de la valeur max() soit l'âge et comparé pour trouver
    for cle_prenom,valeur_age in dictionnaire_de_famille.items():
        if valeur_age >=18:print(cle_prenom,"est majeur, il a",valeur_age,"ans.")
        elif valeur_age <=18:print(cle_prenom,"est mineur, il a",valeur_age,"ans.")
        
old()

