from os import system, name

system("cls") if name == "nt" else system("clear")
vCasa = float(input("Qual o valor da casa? "))
vSalario = float(input("Qual o valor do salário? "))
nPrestacoes = float(input("Quantos anos a pagar? ")) * 12
vPrestacao = vCasa / nPrestacoes
if vPrestacao <= (vSalario * 0.3):
    print(f"A casa pode ser comprada com {nPrestacoes} prestações de R${vPrestacao:.2f}")
else:
    print(f"A casa não pode ser comprada, pois a prestação de R${vPrestacao:.2f} é maior que 30% do salário.")
