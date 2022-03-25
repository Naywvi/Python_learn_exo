"""
Méthode d'instance  : fonction sur une instance (objet)
Méthode de classe   : fonction sur une classe
Méthode statique    : fonction indépendante mais "lié" à une classe 
"""
#Méthode d'instance
# class Humain:
#     def __init__(self, c_nom, c_age):
#         self.nom = c_nom
#         self.age = c_age
    
#     def parler(self, message):
#         print("{} a dit : " .format(self.nom), message)


# h1 = Humain("nagib",23)

# h1.parler("Hello World")
# h1.parler("Are you good ?")

#-----------------------------------------------------------------------------#

#Méthode de classe

# class Humain:

#     lieu_habitation = "Terre"

#     def __init__(self, c_nom, c_age):
#         self.nom = c_nom
#         self.age = c_age
    
#     def parler(self, message):# self -> Méthode standard
#         print("{} a dit : " .format(self.nom), message)
    
#     def changer_planete(cls, nouvelle_planete):#cls -> méthode de class
#         Humain.lieu_habitation = nouvelle_planete#Affectera toute la class
    
#     changer_planete = classmethod(changer_planete)# TRES IMPORTANT , permet de definir la func par une méthode de class. A METTRE DANS LA CLASS
    


# h1 = Humain("nagib",23)

# ##h1.parler("Hello World")
# ##h1.parler("Are you good ?")

# print("planète = {}" .format(Humain.lieu_habitation))
# Humain.changer_planete("Mars")
# print("nouvelle planète = {}" .format(Humain.lieu_habitation))

#-----------------------------------------------------------------------------#

#Méthode static

# class Humain:

#     lieu_habitation = "Terre"

#     def __init__(self, c_nom, c_age):
#         self.nom = c_nom
#         self.age = c_age
    
#     def parler(self, message):# self -> Méthode standard
#         print("{} a dit : " .format(self.nom), message)
    
#     def changer_planete(cls, nouvelle_planete):#cls -> méthode de class
#         Humain.lieu_habitation = nouvelle_planete
    
#     changer_planete = classmethod(changer_planete)

#     def definition():
#         print("bla bla bla")
#     definition = staticmethod(definition)#indépendante de la classe


# #h1 = Humain("nagib",23)

# ##h1.parler("Hello World")
# ##h1.parler("Are you good ?")

# #print("planète = {}" .format(Humain.lieu_habitation))
# #Humain.changer_planete("Mars")
# #print("nouvelle planète = {}" .format(Humain.lieu_habitation))

# Humain.definition()#permet de faire appel à cette méthode n'importe quand

#-----------------------------------------------------------------------------#