import random
delka = int(input("Délka cesty: "))
kroky = int(input("Maximální počet kroků: "))
pozice = int(delka / 2)
cesta = []
for z in range(delka):
    cesta.append(".")
cesta[pozice] = "*"
print("domov",*cesta,"hospoda")
for i in range(kroky):
    cesta = []
    for y in range(delka):
        cesta.append(".")
    r = random.randint(0,1)
    if r == 1:
        pozice = pozice + 1
    else:
        pozice = pozice - 1
    if pozice == -1:
        print("DOMOV*",*cesta,"hospoda")
        print("Skončil jsi doma")
        break
    elif pozice == delka:
        print("DOMOV",*cesta,"*HOSPODA")
        print("Skončil jsi v hospodě")
        break
    else:
        cesta[pozice] = "*"
        print("domov",*cesta,"hospoda")
if i == (kroky - 1):
    print("Usnul jsi na cestě")
input()