from os import system, name

system("cls") if name == "nt" else system("clear")
texto_1 = input("Informe o primeiro texto: ")
texto_2 = input("Informe o segundo texto: ")
final = ""
for letra in texto_1:
    if letra in texto_2 and not letra in final:
        final += letra
if final == "":
    print("Não há caracteres comuns")
else:
    print(f"Caracteres comuns: {final}.")
