from os import system, name

system("cls") if name == "nt" else system("clear")
velocidade = float(input("Qual a velocidade do carro? "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Motorista multado em R${multa:.2f}!")