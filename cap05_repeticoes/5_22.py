from os import system, name

system("cls") if name == "nt" else system("clear")
while True:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    operador = input("Escolha uma operação:\n"
                     "Digite:\n"
                     "1 - para Somar;\n"
                     "2 - para Subtrair;\n"
                     "3 - para Multiplicar;\n"
                     "4 - para Dividir;\n")
    if operador == "1":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operador == "2":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operador == "3":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operador == "4":
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Opção inválida!")
    sair = input("Deseja continuar?\n"
                 "Digite qualquer tecla para continuar, ou;\n"
                 "[X] para Sair.\n").upper()
    if sair == "X":
        print("Calculadora encerrada.")
        break
