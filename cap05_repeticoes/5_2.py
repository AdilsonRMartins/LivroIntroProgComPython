from os import system, name

system("cls") if name == "nt" else system("clear")
x = 50
while x <= 100:
    print(x)
    x = x + 1
