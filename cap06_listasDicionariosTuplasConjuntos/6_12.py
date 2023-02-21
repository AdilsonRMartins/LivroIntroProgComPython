from os import system, name

system("cls") if name == "nt" else system("clear")
L = [1, 7, 2, 4]
menor = L[0]
for e in L:
    if e < menor:
        menor = e
print(menor)
