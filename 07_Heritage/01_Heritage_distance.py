"""
1 - Créer une classe Point, ayant comme paramètres :
    - Un X
    - Un Y
    
   Rajouter à cette class une fonction distance, permettant de connaitre la distance entre deux points.
"""
import random
class Distance:
    """
    Calcul d'une distance
    """
    def __init__(self):
        self.x = random.randint(1,50)
        self.y = random.randint(51,101)
        self.calcul()

    def calcul(self):
        index = 0
        for i in range(self.x,self.y,1):
            index+=1
        print("Il y a {} m entre {}m et {}m .".format(index,self.x,self.y))

Distance()