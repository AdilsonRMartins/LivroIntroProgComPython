from os import system, name

system("cls") if name == "nt" else system("clear")
deposito = float(input("Qual valor do depósito inicial? "))
incremento = float(input("Qual valor dos depósitos mensais? "))
juros = (float(input("Qual a taxa de juros? (Ex.: 3 para 3%) ")) / 100) + 1
mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo * juros + incremento
    print(f"Saldo do mês {mes:02} = {saldo:.2f}")
    mes = mes + 1
print(f"O lucro da aplicação em {mes - 1} meses foi de: R${saldo - deposito - incremento * mes:.2f}.")
