from os import system, name

system("cls") if name == "nt" else system("clear")
texto_1 = input("Informe o texto 1: ")
texto_2 = input("Informe o texto 2: ")
texto_3 = ""
for letra in texto_1:
    if not letra in texto_2:
        texto_3 += letra
print(texto_3)
