from os import system, name

system("cls") if name == "nt" else system("clear")
dividendo = float(input("Informe um dividendo: "))
divisor = float(input("Informe o divisor"))
while dividendo > divisor:
    dividendo -= divisor
    resto = dividendo
print(f"O resto inteiro de {dividendo} / {divisor} = {resto}.")
