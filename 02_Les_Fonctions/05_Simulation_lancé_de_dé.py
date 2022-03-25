#Ecrire une fonction simulant un lancé de dé à 6 faces
import random

#Dessin
def dessin_de(face):
    if face == 1:print(" . . .","\n",". O .","\n",". . .")
    elif face == 2:print(" . O .","\n",". . .","\n",". O .")
    elif face == 3:print(" . O .","\n",". O .","\n",". O .")
    elif face == 4:print(" O . O","\n",". . .","\n","O . O")
    elif face == 5:print(" O . O","\n",". 0 .","\n","O . O")
    elif face == 6:print(" O . O","\n","O . O","\n","O . O")

def lancement_de(inp):
    if inp == "n":
        print("You can try again, bye !")
        return
    elif inp == "y":
        dessin_de(random.randint(1,6))
    else:print("choose 'y' or 'n' in lowercase.")
    return lancement_de(input("You want try again ? [y]/[n]: "))

lancement_de(input("Are you ready ? [y]/[n]: "))
