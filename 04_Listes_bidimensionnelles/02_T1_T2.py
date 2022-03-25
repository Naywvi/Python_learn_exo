#Créer une fonction prenant en paramètres deux chiffres T1 et T2 et retournant une liste de 
#taille T1 contenant dans chaque case une liste de taille T2 remplit de chiffres aléatoires
def start(first,second):
    list_end = []
    for i in range(1,first+1):
        list_end.append(boucle(second))
    return list_end

def boucle(second):
    list_second = []
    for i in range(1,second+1):
        list_second.append(i)
    return list_second

first_inp = int(input("Enter number: "));second_inp = int(input("Enter a second number: "))

print(start(first_inp,second_inp))

#print(define_list())