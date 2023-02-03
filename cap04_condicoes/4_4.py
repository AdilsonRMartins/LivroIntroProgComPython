from os import system, name

system("cls") if name == "nt" else system("clear")
salario = float(input("Qual o valor do salário? "))
if salario > 1250:
    print(f"O valor do aumento é de R${salario * 0.10:.2f}")
if salario <= 1250:
    print(f"O valor do aumento é de R${salario * 0.15:.2f}")
