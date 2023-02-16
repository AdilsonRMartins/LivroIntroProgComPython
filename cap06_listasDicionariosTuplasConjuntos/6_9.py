from os import system, name

system("cls") if name == "nt" else system("clear")
conjunto = [15, 7, 27, 39]
procurado_1 = int(input("Digite o valor a procurar:"))
procurado_2 = int(input("Digite o valor a procurar:"))
achou_1 = False
achou_2 = False
ordem = 0
primeiro = 0
while ordem < len(conjunto):
    if conjunto[ordem] == procurado_1:
        achou_1 = True
        if not achou_2:
            primeiro = 1
    if conjunto[ordem] == procurado_2:
        achou_2 = True
        if not achou_1:
            primeiro = 2
    ordem += 1
if achou_1:
    print(f"{procurado_1} encontrado.")
else:
    print(f"{procurado_1} não encontrado.")
if achou_2:
    print(f"{procurado_2} encontrado.")
else:
    print(f"{procurado_2} não encontrado.")
if primeiro == 1:
    print(f"{procurado_1} foi encontrado primeiro.")
elif primeiro == 2:
    print(f"{procurado_2} foi encontrado primeiro.")
