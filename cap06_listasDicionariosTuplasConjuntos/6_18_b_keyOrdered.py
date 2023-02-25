from os import system, name

system("cls") if name == "nt" else system("clear")
dicionario = {}
caractere = input("Digite uma palavra: ")
for letra in caractere:
    dicionario[letra] = dicionario.get(letra, 0) + 1
print("Keys unordered: " + str(dicionario))
chaves = list(dicionario.keys())
chaves.sort()
dicionario_ordenado = {i: dicionario[i] for i in chaves}
print("Keys ordered: " + str(dicionario_ordenado))
