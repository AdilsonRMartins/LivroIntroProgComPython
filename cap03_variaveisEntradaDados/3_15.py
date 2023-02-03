from os import system, name

system("cls") if name == "nt" else system("clear")
cigarros = int(input("Quantos cigarros você fuma por dia? "))
diasPerdidosPorCigarro = cigarros * 10 / (24 * 60)
anosFumando = float(input("Por quantos anos você já fumou? "))
print(f"Você perderá {(anosFumando * 365 * diasPerdidosPorCigarro)} dias de vida.")
