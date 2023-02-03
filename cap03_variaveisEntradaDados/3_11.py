from os import system, name

system("cls") if name == "nt" else system("clear")
preco = float(input("Informe o preço da mercadoria: "))
desconto = float(input("Informe o percentual de desconto: "))
valorDesconto = preco * (desconto / 100)
preco = preco - desconto
print(f"O preço da mercadoria com desconto é: {preco:.2f}")
