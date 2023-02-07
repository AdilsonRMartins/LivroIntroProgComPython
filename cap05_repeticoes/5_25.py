from os import system, name

system("cls") if name == "nt" else system("clear")
n = float(input("Informe um número: "))
b = 2
while abs(n - b ** 2) > 0.0001:
    p = (b + (n / b)) / 2
    b = p
print(f"A raiz quadadra de {n} é ~ {p:.4f}.")
