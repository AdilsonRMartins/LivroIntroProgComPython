from os import system, name

system("cls") if name == "nt" else system("clear")
texto_1 = input("Informe o primeiro texto: ")
texto_2 = input("Informe o segundo texto: ")
final = ""
for letra in texto_1:
    if not letra in texto_2 and not letra in final:
        final += letra
for letra in texto_2:
    if not letra in texto_1 and not letra in final:
        final += letra
if final == "":
    print("Os caracteres são comuns")
else:
    print(f"Caracteres não comuns: {final}.")
