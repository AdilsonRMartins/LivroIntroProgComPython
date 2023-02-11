from os import system, name

system("cls") if name == "nt" else system("clear")
primeira = []
while True:
    i = input("Digite um valor para a primeira lista (0 para terminar): ")
    if i == "0":
        break
    primeira.append(i)
segunda = []
while True:
    i = input("Digite um valor para a segunda lista (0 para terminar): ")
    if i == "0":
        break
    segunda.append(i)
teste = primeira[:]
teste.extend(segunda)
terceira = []
i = 0
while i < len(teste):
    j = 0
    while j < len(terceira):
        if terceira[j] == teste[i]:
            break
        j += 1
    if j == len(terceira):
        terceira.append(teste[i])
    i += 1
terceira.sort()
print(terceira)
