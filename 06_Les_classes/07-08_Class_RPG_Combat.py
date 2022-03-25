"""
8 - Créer grâce à tout les éléments des exercices précedants, une fonction de Combat entre un PlayerRpg et un Monster
"""
"""
7 - Créer une fonction Attaque pour le PlayerRpg et le Monster, permettant de choisir la prochaine attaque parmis les attaques possibles
"""
"""
6 - Créer une classe Monster ayant comme paramètres :

    Un nom
    Une force
    Une Defense
    Un nombre de points de vie
    Une liste des attaques possibles

"""
"""
5 - Créer une classe Attaque ayant comme pramètres :

    Un nom
    Un pourcentage de chance de toucher
    Des dégats

"""
"""
4 - En continuant l'exercice 3, trouver une solution pour utiliser un objet de l'inventaire du HeroRpg. Il éxiste 3 objets différents :

    Une potion de vie
    Une potion de Force
    Une potion de Defense
"""

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

Inventaire :
0 - popo health
1 - popo strengh
2 - popo defense

Attaque monstre :
"Auto-attaque","Coup de poing","Coup de pied"]
"""
import random
import time
class Player:
    """
    Ceci est un joueur.
    """
    type_define = ["Guerrier","Mage","Assassin","Tank"]
    type_popo = ["health","strengh","defense"]

    def __init__(self,type: int):
        self.type = type
        self.name_type = self.bind_name(self.type)
        self.defense = 0
        self.PV = 0
        self.force = 0
        self.bind_all(type)
        self.inventaire = [0,1,2]

    #Bind name compare with type
    def bind_name(self,type_receive) -> int:
        return self.type_define[type_receive]

    #Bind strengh compare with type
    def bind_all(self,type_receive) -> int:
        if self.type_define[type_receive] == "Guerrier":self.PV = self.bind_rdn(45,60);self.defense=self.bind_rdn(30,40) ;self.force = self.bind_rdn(45,60) 
        elif self.type_define[type_receive] == "Mage":self.PV = self.bind_rdn(20,35);self.defense=self.bind_rdn(5,20) ;self.force = self.bind_rdn(50,70)
        elif self.type_define[type_receive] == "Assassin":self.PV = self.bind_rdn(25,45);self.defense=self.bind_rdn(15,35) ;self.force = self.bind_rdn(70,100)
        elif self.type_define[type_receive] == "Tank":self.PV = self.bind_rdn(70,100);self.defense=self.bind_rdn(75,100) ;self.force = self.bind_rdn(10,25)
    #just randomiser
    def bind_rdn(self,rdn1,rdn2) -> int:
        return random.randint(rdn1,rdn2) 

    #Use Potion
    def Use_popo(self,send_pop):
        if self.inventaire[send_pop] == 0:self.PV += 50
        elif self.inventaire[send_pop] == 1: self.force += 15
        elif self.inventaire[send_pop] == 2: self.defense +=15
        del self.inventaire[send_pop]
        
class Attaque(Player):
    """
    Class d'une attaque.
    """
    def __init__(self):
        self.name_attaque = "Auto-Attaque"
        self.percentage_to_touch = 100
        self.damage = 3

class Monster_one(Player):
    """
    Méga sbire
    """
    lst_attaque = ["Auto-attaque","Coup de poing","Coup de pied"]
    def __init__(self):
        self.name_monster = "Méga sbire"
        self.strengh_of_monster = self.bind_rdn(10,30)
        self.defense_of_monster = self.bind_rdn(30,40)
        self.pv_of_monster = self.bind_rdn(100,120)
        self.attaque_returned = self.attaque(self.bind_rdn(0,2))
    def attaque(self, attaque_id):
        return self.lst_attaque[attaque_id]

class Action(Player and Attaque):
    """
    Action -> attaque
    """
    def __init__(self):
        self.start()
    
    def start(self):
        print("\nVous disposez de {} comme attaque. Pour {} pv de dégats et {}% de chances d'être réussie.\n".format(at.name_attaque,at.damage,at.percentage_to_touch))
        inp = input("Voulez vous utiliser {} contre {}? [y]/[n]".format(at.name_attaque,am.name_monster))
        if inp == "y": self.attaquer()
        else:print("Vous ne faite rien.");self.il_attaque()
    def attaquer(self):
        am.pv_of_monster -= at.damage
        print("\n===\nVous avez retirer {} pv à {}.Il lui reste {} pv.\n".format(at.damage,am.name_monster,am.pv_of_monster))
        time.sleep(1)
        print("\nAttendez, il réplique ...\n")
        time.sleep(0.5)
        print("{} vous attaque avec {}.".format(am.name_monster,am.attaque_returned))
        a.PV -= am.strengh_of_monster
        print("Vous avez perdu {} pv. Il vous reste {} pv.\n===\n".format(am.strengh_of_monster,a.PV))
    
    def il_attaque(self):
        print("\n===\nAttendez, il attaque ...\n")
        time.sleep(0.5)
        print("{} vous attaque avec {}.".format(am.name_monster,am.attaque_returned,))
        a.PV -= am.strengh_of_monster
        print("Vous avez perdu {} pv. Il vous reste {} pv.\n===\n".format(am.strengh_of_monster,a.PV))
        
a = Player(1)
print("type int:",a.type,"|defense:",a.defense,"|pv:",a.PV,"|force:",a.force,"|nom: ",a.name_type,"|inventaire:",a.inventaire)
a.Use_popo(2)
print("type int:",a.type,"|defense:",a.defense,"|pv:",a.PV,"|force:",a.force,"|nom: ",a.name_type,"|inventaire:",a.inventaire)
at = Attaque()
print("nom :",at.name_attaque,"|pourcentage : ",at.percentage_to_touch,"|damage : ",at.damage)

am = Monster_one()
print("nom :",am.name_monster,"|force :",am.strengh_of_monster,"|defense :",am.defense_of_monster,"|pv :",am.pv_of_monster,"|attaque :",am.attaque_returned)
while True:
    Action()
#Flemme de faire le calcul de l'attaque avec la force ect ... & la "force" des attaques. Mais faisable (-> to ez)