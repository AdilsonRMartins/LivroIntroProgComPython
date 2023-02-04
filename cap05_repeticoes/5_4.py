from os import system, name

system("cls") if name == "nt" else system("clear")
fim = int(input("Digite o último número a imprimir: "))
x = 1
while x <= fim:
    print(x)
    x = x + 2
