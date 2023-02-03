from os import system, name

system("cls") if name == "nt" else system("clear")
distancia = float(input("Quantos Km foram percorridos? "))
diasDeAluguel = int(input("Por quantos dias o carro foi alugado? "))
precoDia = 60
precoKm = 0.15
precoFinal = diasDeAluguel * precoDia + distancia * precoKm
print(f"Percorrer {distancia:.1f}km por {diasDeAluguel} dias de aluguel custou R${precoFinal:.2f}.")
