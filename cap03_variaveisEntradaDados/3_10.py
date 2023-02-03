from os import system, name

system("cls") if name == "nt" else system("clear")
salario = float(input("Informe o valor do salário: "))
aumento = float(input("Informe o percentual do aumento: "))
valorAumento = salario * (aumento / 100)
salario = salario + valorAumento
print(f"O novo salário é de: {salario:.2f}")
