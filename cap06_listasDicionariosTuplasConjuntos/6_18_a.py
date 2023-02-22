from os import system, name

system("cls") if name == "nt" else system("clear")
dicionario = {}
caractere = input("Digite uma palavra: ")
for letra in caractere:
    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1
print(dicionario)


