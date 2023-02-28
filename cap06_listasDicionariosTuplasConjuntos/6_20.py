from os import system, name

system("cls") if name == "nt" else system("clear")
a = {4, 2, 5, 6, 7}
b = {5, 6, 7, 8, 2, 3}
print("Não mudaram: " + str(a & b))
print("Novos: " + str(b - a))
print("Não foram removidos: " + str(b & a))
