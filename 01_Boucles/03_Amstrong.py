#Ecrire un programme détectant les nombres de Armstrong compris entre 0 et 999.

#Version moche

for i in range(10):
    for j in range(10):
        for k in range(10):
            if i**3+ j**3 + k**3 == i+j*10 +k*100:
                print(i,j,k)

#Version belle
for i in range(1000):
    U =1%10
    D = (i//10)%10
    C = i//100
    if i == U**3 +D**3 +C**3:
        print(i)