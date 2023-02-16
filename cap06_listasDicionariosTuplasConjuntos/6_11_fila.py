from os import system, name

system("cls") if name == "nt" else system("clear")
L = []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)
for x in L:
    print(x)
