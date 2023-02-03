from os import system, name

system("cls") if name == "nt" else system("clear")
dias = int(input("Informe o número de dias: "))
horas = int(input("Informe o número de horas: "))
minutos = int(input("Informe o número de minutos: "))
segundos = int(input("Informe o número de segundos: "))
print(f"A informação representa {dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos} segundos")
