from os import system, name

system("cls") if name == "nt" else system("clear")
salário = 750
aumento = 15
print(salário + (salário * aumento / 100))