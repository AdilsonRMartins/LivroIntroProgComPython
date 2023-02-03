from os import system, name

system("cls") if name == "nt" else system("clear")
distancia = float(input("Quantos KM a percorrer? "))
velocidade = float(input("Qual a velocidade média esperada para a viagem? "))
tempo = distancia / velocidade
input(f"A viagem levará {tempo:.1f} horas.")
