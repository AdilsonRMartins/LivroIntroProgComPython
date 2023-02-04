from os import system, name

system("cls") if name == "nt" else system("clear")
tabuada = int(input("Informe a tabuada: "))
x = 1
while x <= 10:
    print(f"{tabuada} * {x} = {tabuada * x}")
    x = x + 1
