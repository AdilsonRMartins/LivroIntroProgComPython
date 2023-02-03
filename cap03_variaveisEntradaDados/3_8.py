from os import system, name

system("cls") if name == "nt" else system("clear")
metros = float(input("Informe um valor em metros: "))
print(f"O valor representa {(metros * 100):.2f} centímetros.")
