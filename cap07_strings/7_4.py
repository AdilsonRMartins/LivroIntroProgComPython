from os import system, name

system("cls") if name == "nt" else system("clear")
texto = input("Informe o texto: ")
contador = {}
for letra in texto:
    contador[letra] = contador.get(letra, 0) + 1
for chave, valor in contador.items():
    print(f"{chave}: {valor}x.")
