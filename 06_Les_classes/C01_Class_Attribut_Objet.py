"""
Classe      : plan de conception, genre (ex: Humain)
Objet       : instance d'une classe (ex: Julien, est un objet de la classe Humain)
Attribut    : variable de classe (ex: prenom, âge, taille, sexe ...)


/!\ self appartient à, comme une déclaration de variable ciblé (enregistré en mémoire, rattacher à)
/!\ Un attribut de classe est une "variable non propre" soit unviverselle à la classe pour chaque instance
"""
#class Humain:
#    """
#    Classe des êtres humain #Définition de la classe
#    """
#    def __init__(self):
#        print("Création d'un humain ...",self)#<--- son emplacement,similaire à & | * (pointeur golang)
#        #pass#PASS Signifie (passer outre)
#print("Lancement du programme ...")

#h1 = Humain()#Création d'un objet
#h2 = Humain()


#-----------------------------------------------------------------------------#
# /!\ "def __init__(self):" s'appel un constructeur

#class Humain:
#    """
#    Classe des êtres humain
#    """
#    def __init__(self):
#        print("Création d'un humain ...")
#        self.prenom = "Nagib"
#        self.age = 1
        
#print("Lancement du programme ...")

#h1 = Humain()
#print(">",h1.prenom) 
#print("> le prénom est -> {}" .format(h1.prenom))#Pour une meilleure insertion
#h2 = Humain()

#-----------------------------------------------------------------------------#

#Ici on prend juste en parametre dans le constructeur, comme dans une fonction.

#def __init__(self,c_prenom, c_age="1") <--- Ici on donne juste un âge par défault, mais il peut ê remplacé si défini ensuite

#class Humain:
#    def __init__(self,c_prenom, c_age=1):#"c_" pour classe ...
#        self.prenom = c_prenom 
#        self.age = c_age

#h1 = Humain("prenom")
#h2 = Humain("toto",10)

#print(">",h1.prenom,h1.age)
#print("> {} {}" .format(h2.prenom,h2.age))

#h1.prenom = "prenom2" #Possibilité de changer le prenom par la suite
#print(">",h1.prenom)

#-----------------------------------------------------------------------------#

# /!\ Un attribut de classe est une "variable non propre" soit unviverselle à la classe pour chaque instance

# class Humain:

#     humains_crees = 0 # ICI

#     def __init__(self,c_prenom, c_age=1):
#         self.prenom = c_prenom 
#         self.age = c_age
#         Humain.humains_crees +=1# BIM +1

# h1 = Humain("prenom")
# h2 = Humain("toto",10)

# print(">",h1.prenom,h1.age)
# print("> {} {}" .format(h2.prenom,h2.age))
# print("> Nombre d'humains crée {}" .format(Humain.humains_crees))

#-----------------------------------------------------------------------------#
