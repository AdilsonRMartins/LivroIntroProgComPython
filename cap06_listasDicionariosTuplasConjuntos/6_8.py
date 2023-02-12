from os import system, name

system("cls") if name == "nt" else system("clear")
conjunto = [15, 7, 27, 39]
procurado = int(input("Digite o valor a procurar:"))
posicao = 0
while posicao < len(conjunto):
    if conjunto[posicao] == procurado:
        break
    posicao += 1
if posicao < len(conjunto):
    print(f"{procurado} achado na posição {posicao}")
else:
    print(f"{procurado} não encontrado")
