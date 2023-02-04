from os import system, name

system("cls") if name == "nt" else system("clear")
distancia = float(input("Quantos Km deseja percorrer? "))
preco = 0
if distancia > 200:
    print(f"O preço é {distancia * 0.45:.2f}, R$0,45/Km")
else:
    print(f"O preço é {distancia * 0.5:.2f}, R$0,50/Km")
