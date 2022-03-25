#Créer une fonction prenant une liste en entrée et la transformant pour lui enlever les valeurs 0
def looptoremove(inp):
    for i in inp:
        if i == "0":
            inp.remove('0')
    return inp

print(looptoremove(list(input('Write a long number : '))))