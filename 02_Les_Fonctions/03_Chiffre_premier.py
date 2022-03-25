#Créer une fonction qui répond oui ou non au fait que le paramètre donné soit un chiffre premier ou pas

def premier(inp):
    for i in range(4,inp,1):
        c = inp%i
        if c == 0:print("non");break#si modulo de i renvoie 0
        elif i==inp-1:print("oui")#sinon premier
    return premier(int(input("Choisissez à nouveau un paramètre :")))

premier(int(input("Choisissez un paramètre:")))