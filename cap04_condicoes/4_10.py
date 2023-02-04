from os import system, name

system("cls") if name == "nt" else system("clear")
consumo = int(input("Qual foi o consumo em kWh? "))
instalacao = input("Qual o tipo de instalação?\n"
                   "Digite:\n"
                   "[R] para residências;\n"
                   "[I] para insdústrias;\n"
                   "[C] para comércios. ").upper()
preco = 0
if instalacao == "R":
    if consumo > 500:
        preco = consumo * 0.65
    else:
        preco = consumo * 0.40
elif instalacao == "I":
    if consumo > 5000:
        preco = consumo * 0.6
    else:
        preco = consumo * 0.55
elif instalacao == "C":
    if consumo > 1000:
        preco = consumo * 0.6
    else:
        preco = consumo * 0.55
else:
    print("Digite uma opção válida.")
print(f"O preço é: R${preco:.2f}")
