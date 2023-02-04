from os import system, name

system("cls") if name == "nt" else system("clear")
deposito = float(input("Qual  depósito inicial? "))
juros = (float(input("Qual a taxa de juros? (Ex.: 3 para 3%) ")) / 100) + 1
print(juros)
mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo * juros
    print(f"Saldo do mês {mes:02} = {saldo:.2f}")
    mes = mes + 1
print(f"O lucro da aplicação em {mes - 1} meses foi de: R${saldo - deposito:.2f}.")
