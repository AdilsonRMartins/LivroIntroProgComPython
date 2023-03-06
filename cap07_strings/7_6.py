from os import system, name

system("cls") if name == "nt" else system("clear")
texto_1 = input("Informe o texto 1: ")
texto_2 = input("Informe o texto 2: ")
texto_3 = input("Informe o texto 3: ")
final = ""
if len(texto_2) == len(texto_3):
    for letra in texto_1:
        indice = texto_2.find(letra)
        if indice > (-1):
            final += texto_3[indice]
        else:
            final += letra
    if final == "":
        print("Não foi informado o Texto 1")
    else:
        print(f"Os caracteres '{texto_2}' foram substtituídos por '{texto_3}' em '{texto_1}', resultando em '{final}'")
else:
    print("Texto 2 e Texto 3 precisam ter o mesmo número de caracteres.")
