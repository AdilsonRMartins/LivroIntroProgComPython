from os import system, name

system("cls") if name == "nt" else system("clear")
lista1 = []
lista2 = []
while True:
    item = input("Digite um valor para a primeira lista (0 para terminar): ")
    if item == "0":
        break
    lista1.append(item)
while True:
    item = input("Digite um valor para a segunda lista (0 para terminar): ")
    if item == "0":
        break
    lista2.append(item)
lista3 = lista1[:]
lista3.extend(lista2)
item = 0
print(lista3)
