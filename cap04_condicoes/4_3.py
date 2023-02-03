from os import system, name

system("cls") if name == "nt" else system("clear")
a = int(input("Digite um valor: "))
b = int(input("Digite um segundo valor: "))
c = int(input("Digite um terceiro valor: "))
maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f"O maior é o {maior}, e o menor é o {menor}")
