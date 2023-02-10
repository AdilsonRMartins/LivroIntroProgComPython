from os import system, name

system("cls") if name == "nt" else system("clear")
notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 7:
    notas[x] = int(input(f"Informe a {x + 1}° nota: "))
    x += 1
x = 0
while x < 7:
    soma += notas[x]
    x += 1
print(f"Média: {soma / x:5.2f}")
