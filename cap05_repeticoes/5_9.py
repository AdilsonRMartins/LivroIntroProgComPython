from os import system, name

system("cls") if name == "nt" else system("clear")
dividendo = int(input("Informe um dividendo: "))
divisor = int(input("Informe um divisor: "))
x = dividendo
quociente = 0
while x >= divisor:
    quociente = quociente + 1
    x = x - divisor
    resto = x
print(f"Divisão inteira = {dividendo} / {divisor} = {quociente}")
print(f"Resto = {dividendo} / {divisor} = {resto}")
