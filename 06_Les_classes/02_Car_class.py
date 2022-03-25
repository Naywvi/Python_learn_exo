"""
2 - Créer une classe Car ayant comme paramètres :

    Sa vitesse maximale
    Sa vitesse actuelle
    Sa distance parcourue
    Sa consomation en carburant
    Son carburant actuel
    Le nombre de personnes pouvant rentrer dans la voiture
    Les personne actuellement présentes dans la voiture

et ayant comme fonctions :

    Une fonction permettant de rajouter une personne dans la voiture
    Une fonction permettant de retirer une personne de la voiture
    Une fonction faisant avancer la voiture
"""

import random
import time

class Car:
    """
    La voiture :3
    """
    people = ["Martin","Julienne","Paupiette","Marie-Antoinette","Le chien","Le chat","Maman","Papa","la moche"]

    def __init__(self):
        print("Votre voiture est en construction ...")
        self.vitesse_max = random.randint(160,260)
        self.vitesse_actuelle = random.randint(0,self.vitesse_max)
        self.distance_parcourue = random.randint(0,400000)
        self.consommation = round(random.uniform(0.4,0.7),3) #Pour 1km en
        self.carburant_actuel = random.randint(15,50)
        self.nombre_de_place = random.randint(2,6)

        self.qui_est_dedans = self.qui_est_DEDANS()
    
    def qui_est_DEDANS(self):
        occupant_voiture = []
        for _ in range(1,self.nombre_de_place,1):
            random_people = random.randint(0,len(self.people)-1)
            occupant_voiture.append(self.people[random_people])
            del self.people[random_people]
        return occupant_voiture
    
    def add(self):
        self.place()
        time.sleep(1.5)
        if self.nombre_de_place == len(self.qui_est_dedans):print("La voiture est pleine.")
        else:
            rdn = random.randint(0,len(self.people)-1)
            self.qui_est_dedans.append(self.people[rdn])
            print("{} monte dans la voiture." .format(self.people[rdn]))
            del self.people[rdn]
        time.sleep(1.5)
        self.place()

    def remove_p(self):
        
        if len(self.qui_est_dedans)-1 == 0: time.sleep(1);print("Impossible de retirer quelqu'un, sinon la voiture va être vide. MAIS QUI VA LA CODUIRE ?")
        else:
            rdn = random.randint(0,len(self.qui_est_dedans)-1)
            one_people = self.qui_est_dedans[rdn]
            self.people.append(one_people)
            print("{} sort de la voiture." .format(one_people))
            del self.qui_est_dedans[rdn]
        time.sleep(1.5)
        self.place()

    def place(self):
        print("Il y a {} personne(s) dans la voiture, pour {} places." .format(len(self.qui_est_dedans),self.nombre_de_place))
    
    def moove(self, inp):
        input("Appuie sur une touche pour démarer la voiture.")
        print("Démarage de la voiture ...")
        index = 0
        while True:
            
            vitesse = random.randint(self.vitesse_actuelle, self.vitesse_actuelle+10)
            print("votre vitesse actuelle {} km/heures".format(vitesse))
            index +=1
            time.sleep(1)
            if index == 3:
                n = input('Donner une direction (stop pour stoper la voiture): ')
                index = 0
                if n == "stop":
                    print("La voiture s'arrête\n")
                    return

def select(list_vt):
    index = 0
    for i in list_vt:
        print(index,"-",list_vt[index])
        index += 1
        selection = list_vt[int(input("Choisissez une voiture :"))]

    return selection
            

def start():
    start_inp = input("Voulez-vous crée une nouvelle voiture ? [y]/[n]")
    liste_de_voiture_cree = []
    if start_inp == "y" or start_inp == "yes" or start_inp == "Y" or start_inp == "YES":
        nom_voiture = input("Donner lui un nom :")
        liste_de_voiture_cree.append(nom_voiture)
        voiture_selectionner = select(liste_de_voiture_cree)
        nom = voiture_selectionner
        voiture_selectionner = Car()
    
        #Définission de la voiture crée :
        print("\nLa carte grise de {} ." .format(nom))
        print("{} a parcourue {} km.".format(nom,voiture_selectionner.distance_parcourue))
        print("{} consomme {}€ /minute".format(nom,voiture_selectionner.consommation))
        print("{} contient {} places pour un reservoir de {} L .".format(nom,voiture_selectionner.nombre_de_place,voiture_selectionner.carburant_actuel))

        time.sleep(1)
        print("\nAttendez, des gens montent dedans ...\n")
        time.sleep(1.5)
        
        if len(voiture_selectionner.qui_est_dedans) <= 1:print("{} est monté dans la voiture." .format(" ".join(voiture_selectionner.qui_est_dedans)))
        else:print("{} sont monté dans la voiture.\n" .format(" et ".join(voiture_selectionner.qui_est_dedans)))

        while True:
            time.sleep(1)
            retirer_rajouter = input("Voulez-vous plutôt: \n- retirer ou ajouter quelqu'un dans la voiture. \n- faire avancer la voiture ?\n(stop pour arreter la voiture) ... : ")
            print("\n")
            if retirer_rajouter == "retirer":voiture_selectionner.remove_p()
            elif retirer_rajouter == "rajouter" or retirer_rajouter == "ajouter":voiture_selectionner.add()
            elif retirer_rajouter == "avancer":voiture_selectionner.moove(0)
            elif retirer_rajouter == "stop":print("\nLa voiture ralentit.");time.sleep(1);return
    else:return

start()