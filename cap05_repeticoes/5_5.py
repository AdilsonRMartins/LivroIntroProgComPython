from os import system, name

system("cls") if name == "nt" else system("clear")
x = 1
while x <= 10:
    print(x * 3)
    x = x + 1
