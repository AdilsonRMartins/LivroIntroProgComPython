from os import system, name

system("cls") if name == "nt" else system("clear")
num1 = float(input("Informe um número: "))
num2 = float(input("Informe um segundo número: "))
resultado = 0
operacao = input("Qual operação deseja realizar?\n"
                 "Digite:\n"
                 "[+] para soma;\n"
                 "[-] para subtração;\n"
                 "[*] para multiplicação; ou\n"
                 "[/] para divisão. ")
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
else:
    resultado = num1 / num2
print(f"O resultado da operação {num1:.1f} {operacao} {num2:.1f} = {resultado:.1f}")
