from os import system, name

system("cls") if name == "nt" else system("clear")
numero = int(input("Quantos números primos deseja? "))
resultado = ""
if numero < 1:
    print("Não há números primos neste intervalo.")
if numero == 1:
    print(f"Apresentando {numero} números primos: 2.")
else:
    contador = 1
    teste = 3
    while contador < numero:
        divisor = 3
        while divisor <= teste:
            if teste % divisor == 0:
                break
            divisor += 2
        if teste == divisor:
            resultado = resultado + ", " + str(teste)
            contador += 1
        teste += 1
    print(f"Apresentando {numero} números primos: 2{resultado}.")
