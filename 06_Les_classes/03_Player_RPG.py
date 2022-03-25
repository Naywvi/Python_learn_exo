"""
3 - Créer une classe PlayerRPG ayant comme paramètres :

    Un type
    Une force
    Une Defense
    Un nombre de points de vie
    Une liste d'objets

Créer le constructeur de PlayerRPG qui ne prend en paramètre qu'une seule chose, le type de Hero (Guerrier, Mage, etc)

Créer une fonction permettant d'ouvrir son inventaire (afficher la liste des objets)

type:
0 - Guerrier
1 - Mage
2 - Assasins
3 - Tank
"""
import random
class Player:
    """
    Ceci est un joueur.
    """
    type_define = ["Guerrier","Mage","Assassin","Tank"]

    def __init__(self,type: int):
        self.type = type
        self.name_type = self.bind_name(self.type)
        self.defense = 0
        self.PV = 0
        self.force = 0
        self.bind_all(type)
        self.inventaire = {}

    #Bind name compare with type
    def bind_name(self,type_receive) -> int:
        return self.type_define[type_receive]

    #Bind strengh compare with type
    def bind_all(self,type_receive) -> int:
        if self.type_define[type_receive] == "Guerrier":self.PV = self.bind_rdn(45,60);self.defense=self.bind_rdn(30,40) ;self.force = self.bind_rdn(45,60) 
        elif self.type_define[type_receive] == "Mage":self.PV = self.bind_rdn(20,35);self.defense=self.bind_rdn(5,20) ;self.force = self.bind_rdn(50,70)
        elif self.type_define[type_receive] == "Assassin":self.PV = self.bind_rdn(25,45);self.defense=self.bind_rdn(15,35) ;self.force = self.bind_rdn(70,100)
        elif self.type_define[type_receive] == "Tank":self.PV = self.bind_rdn(70,100);self.defense=self.bind_rdn(75,100) ;self.force = self.bind_rdn(10,25)

    def bind_rdn(self,rdn1,rdn2) -> int:
        return random.randint(rdn1,rdn2) 

a = Player(0)
print("type int:",a.type,"|defense:",a.defense,"|pv:",a.PV,"|force:",a.force,"|nom: ",a.name_type)