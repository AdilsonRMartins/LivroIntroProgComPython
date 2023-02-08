from os import system, name

system("cls") if name == "nt" else system("clear")
num = (input("Informe um número: "))
indice1 = len(num) - 1
indice2 = 0
while indice2 > indice1 and num[indice1] == num[indice2]:
    indice1 -= 1
    indice2 += 1
if num[indice1] == num[indice2]:
    print(f"O número {num} é palíndromo.")
else:
    print(f"O número {num} não é palíndromo.")
