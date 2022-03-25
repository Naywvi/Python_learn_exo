#Créer une fonction retournant une liste de dix cases chacune contenant une autre liste 
#de 10 cases remplit par la valeur de l’indice de la première liste plus celui de la deuxième
def define_list():
    def boucle():
        listinp = []
        for i in range(1,11):
            listinp.append(i)
        return listinp
    first_list = []
    for i in range(1,11):
        first_list.append(boucle())
    return first_list

print(define_list())