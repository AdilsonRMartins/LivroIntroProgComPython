from os import system, name

system("cls") if name == "nt" else system("clear")
T = [-10, -8, 0, 1, 2, 5, -2, -4]
menor = T[0]
maior = T[0]
for e in T:
    if e < menor:
        menor = e
    if e > maior:
        maior = e
media = (maior + menor) / 2
print("Menor temperatura: " + str(menor))
print("Maior temperatura: " + str(maior))
print("Temperatura média: " + str(media))
