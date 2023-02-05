from os import system, name

system("cls") if name == "nt" else system("clear")
total = 0
preco = 0
invalido = 1
while True:
    codigo = input("Digite o código do produto: ")
    if codigo == "1":
        preco = 0.50
    elif codigo == "2":
        preco = 1.0
    elif codigo == "3":
        preco = 4.0
    elif codigo == "5":
        preco = 7.0
    elif codigo == "9":
        preco = 8.0
    elif codigo == "0":
        break
    else:
        invalido = 0
    if invalido != 0:
        quantidade = int(input(f"Informe a quantidade do item cód. {codigo}: "))
        total = total + quantidade * preco
        print(
            f"Cód. {codigo} - R$/un. {preco:.2f} x Qntd. {quantidade} = {preco * quantidade:.2f} - Total parcial: {total:.2f}")
        preco = 0
    else:
        print(f"\nCód. {codigo} - inválido!\n")
        invalido = 1
print(f"\nTotal da compra: R${total:.2f}\n")
