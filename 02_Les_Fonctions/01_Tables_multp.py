#Ecrire une fonction qui prend en paramètre un texte et l'affiche 10 fois.
#si le chiffre et négatif ou sa table de multiplication si il est positif
def calcul(inp):
    if inp < 0:
        print("error")
        return
    for i in range (1,11,1):
        print(inp,"x",i,"=",inp*i)

calcul(int(input("Entrée le nombre ou chiffre à multiplier : ")))