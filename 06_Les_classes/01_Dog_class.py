"""
1 - Créer une classe Dog, ayant comme paramètres :

    Un nom
    Un age
    Un ou plusieurs propriétaires
    Une liste des "tricks" qu'a appris le chien

La classe chien a aussi plusieurs fonctions :

    Une fonction "Learn" permettant de rajouter un trick
    Une fonction de comparaison permettant de connaitre les tricks en commun avec un autre chien

"""

"""
Liste de tricks:
1> donner la pâte 
2> se coucher
3> faire le mort
4> faire le beau
5> aller chercher la balle
6> voler de l'argent chez les voisins
"""
import random

class Dog:
    """
    class de chien :3
    """
    
    def __init__(self, c_nom, c_age, c_proprio):
        self.nom = c_nom
        self.age = c_age
        self.propio = c_proprio

    def boucle_tricks(self):
        result = []
        for i in range(1,random.randint(1,6),random.randint(1,4)):
            result.append(i)
        self.result = result
    
    def learn(self, list_learn):
        
        result_learning = []
        
        for i in list_learn:

            if i == 1:result_learning.append("donner la pâte\n")
            elif i == 2:result_learning.append("se coucher\n")
            elif i == 3:result_learning.append("faire le mort(e)\n")
            elif i == 4:result_learning.append("faire le beau\n")
            elif i == 5:result_learning.append("aller chercher la balle\n")
            elif i == 6:result_learning.append("voler de l'argent chez les voisins :D\n")

        if len(result_learning) == 0:result_learning.append("RIEN faire, un chien éclaté au sol ...\n")
        elif len(result_learning) >= 2:result_learning.append("\nUn bon chien !\n")
        elif len(result_learning) >= 4:result_learning.append("\nUn SUPER chien !\n")
        elif len(result_learning) == 6:result_learning.append("\nLe meilleur chien !\n")

        self.result_end_learning = result_learning
        
    def similitude(self,un, le_reste):

        self.similitude_lst = []
        for i in le_reste:
            for j in un:
                if i == j:self.similitude_lst.append(j)
        
        return self.similitude_lst

    def printer(self,send,poo):
        lst_end_similitude = []
        index = 0
        for i in send:
            lst_end_similitude.append(poo[index])
            index +=1
        if len(lst_end_similitude) == 0:lst_end_similitude.append("aucune =)\n")
        return "".join(lst_end_similitude)
    

dog1 = Dog("Xena",random.randint(2,20),["Monsieur Pierro", " et ", "Madame Pierra"])#flemme pour le "et"
dog1.boucle_tricks()
dog1.learn(dog1.result)

dog2 = Dog("Lutin",random.randint(2,20),["Madame Machine"])
dog2.boucle_tricks()
dog2.learn(dog2.result)

dog3 = Dog("Perlin",random.randint(2,20),["personne"])
dog3.boucle_tricks()
dog3.learn(dog3.result)

#
skils1_2 = dog1.similitude(dog1.result,dog2.result)
skils1_3 = dog1.similitude(dog1.result,dog3.result)

#
skils2_1 = dog2.similitude(dog2.result,dog1.result)
skils2_3 = dog2.similitude(dog2.result,dog3.result)

#
skils3_1 = dog3.similitude(dog3.result,dog1.result)
skils3_2 = dog3.similitude(dog3.result,dog2.result)
#
print("--------------\n","\n{} a {} ans elle appartient à {}.\n" .format(dog1.nom,dog1.age,"".join(dog1.propio)))
print("Elle sait : \n{}".format("".join(dog1.result_end_learning)))
print("Les similitudes au niveau des skils appris avec Lutin sont : \n{}" .format(dog1.printer(skils1_2,dog1.result_end_learning)))
print("Et les similitudes avec Perlin sont : \n{}" .format(dog1.printer(skils1_3,dog1.result_end_learning)),"\n--------------\n")

print("{} a {} ans il appartient à {}.\n" .format(dog2.nom,dog2.age,"".join(dog2.propio)))
print("Il sait : \n{}".format("".join(dog2.result_end_learning)))
print("Les similitudes au niveau des skils appris avec Lutin sont : \n{}" .format(dog2.printer(skils2_1,dog2.result_end_learning)))
print("Et les similitudes avec Perlin sont : \n{}" .format(dog2.printer(skils2_3,dog2.result_end_learning)),"\n--------------\n")

print("{} a {} ans iel appartient à {}.\n" .format(dog3.nom,dog3.age,"".join(dog3.propio)))
print("Iel sait : \n{}".format("".join(dog3.result_end_learning)))
print("Les similitudes au niveau des skils appris avec Lutin sont : \n{}" .format(dog3.printer(skils3_1,dog3.result_end_learning)))
print("Et les similitudes avec Perlin sont : \n{}" .format(dog3.printer(skils3_2,dog3.result_end_learning)),"\n--------------\n")

"""
.format()           : ajoute à "(}" dans un print("{}")
foo                 : similaire à nil/null
"".join(...)        : strconv
"""