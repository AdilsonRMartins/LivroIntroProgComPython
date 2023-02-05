from os import system, name

system("cls") if name == "nt" else system("clear")
soma = 0
contador = 0
while True:
    num = int(input("Digite um número inteiro: "))
    if num == 0:
        break
    else:
        soma += num
        contador += 1
print(f"{contador} números foram digitados.")
print(f"A soma dos número é igual a {soma}")
print(f"A média aritmética dos números é {soma / contador:.1f}")
