from os import system, name

system("cls") if name == "nt" else system("clear")
num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe um segundo número inteiro: "))
print(f"A soma dos dois número é: {num1 + num2}")
