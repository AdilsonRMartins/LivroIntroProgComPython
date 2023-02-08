from os import system, name

system("cls") if name == "nt" else system("clear")
num = (input("Informe um número: "))
contador = 0
palindromo = ""
teste = int(num)
while contador < len(num):
    resto = teste % 10
    palindromo = palindromo + str(resto)
    teste = teste // 10
    contador += 1
resultado = "não é"
if num == palindromo:
    resultado = "é"
print(f"O número {num} {resultado} um palíndromo")
