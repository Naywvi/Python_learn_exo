#Créer une fonction créant une liste de 20 cases chacune remplit par l’indice de la case
def listdelist():
    listdl = []
    for i in range(1,21,1):
        listdl.append([i])
    return listdl
print(listdelist())