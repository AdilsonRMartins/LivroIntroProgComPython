from os import system, name

system("cls") if name == "nt" else system("clear")
x = 10
while x >= 0:
    print(x)
    x = x - 1
print("Fogo!")
