#Ecrire un programme qui prend un chiffre donné par l'utilisateur (positif ou négatif)
#et qui affiche tous les nombres compris entre ce nombre et zero


def calcul(nb_send):
    neg = 0
    if nb_send < 0:nb_send *= -1;neg = 1
    for i in range(nb_send,0,-1):
        if neg == 1:print(i*-1)
        else:print(i)
    print("0")

calcul(int(input("Choisit un nombre ou un chiffre: ")))