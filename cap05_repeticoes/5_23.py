from os import system, name

system("cls") if name == "nt" else system("clear")
numero = int(input("Informe um número: "))
if numero <= 1:
    resposta = "não é"
else:
    if numero == 2:
        resposta = "é"
    elif numero % 2 == 0:
        resposta = "não é"
    else:
        divisor = 3
        while divisor < numero:
            if numero % divisor == 0:
                break
            divisor += 2
        if numero == divisor:
            resposta = "é"
        else:
            resposta = "não é"
print(f"{numero} {resposta} um número primo.")
