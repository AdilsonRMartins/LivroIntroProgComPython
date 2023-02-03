from os import system, name

system("cls") if name == "nt" else system("clear")
celsius = float(input("Informe a temperatura em Celsius: "))
fahrenheit = celsius * 1.8 + 32
print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F.")
