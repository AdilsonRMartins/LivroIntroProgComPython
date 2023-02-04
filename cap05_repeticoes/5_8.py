from os import system, name

system("cls") if name == "nt" else system("clear")
tabuada = int(input("Informe a tabuada: "))
multiplos = int(input("Informe a quantidade de múltiplos: "))
x = 1
resultado = 0
while x <= multiplos:
    resultado = resultado + tabuada
    x = x + 1
print(f"{tabuada} * {multiplos} = {resultado}")
