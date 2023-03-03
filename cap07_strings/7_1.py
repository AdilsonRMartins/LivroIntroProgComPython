from os import system, name

system("cls") if name == "nt" else system("clear")
texto_1 = input("Informe o primeiro texto: ")
texto_2 = input("Informe o segundo texto: ")
print(texto_1.find(texto_2))
