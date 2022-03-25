#Boucle input x10
def Printer(): 
    Acc= []
    for i in range(0,10,1):
        Acc.append(input("Enter number : "))
    return Acc

#ReOrder [] croissant
def ReOrder(inp):
    print(sorted(inp, key=int, reverse=True))

ReOrder(Printer())