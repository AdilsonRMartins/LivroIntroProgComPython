from os import system, name

system("cls") if name == "nt" else system("clear")
tabuada = int(input("Informe a tabuada: "))
multiplos = int(input("Informe a quantidade de múltiplos: "))
x = 1
while x <= multiplos:
    print(f"{tabuada} * {x} = {tabuada * x}")
    x = x + 1
