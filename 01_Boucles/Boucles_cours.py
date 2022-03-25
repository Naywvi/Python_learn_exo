#Boucle while "tant que la condition est vraie on continue"
mdp ="azert"
txt = input()

while mdp != txt:
    txt=input()
print("Logged")
#---------------------------------------------------------------------------------------------------#
#Boucle for range = for each "itère sur l'ensemble de données d'une variable"
s = "abcdef"
for c in s:
    print(c)
#boucle for normal
for i in range(0,10,1):#ou range(10)
    print(i)
#Ici range(0,10,1) 0 pour le début | 10 la fin | ++ itération
#---------------------------------------------------------------------------------------------------#