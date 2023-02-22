from os import system, name

system("cls") if name == "nt" else system("clear")
estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.50]}
total = 0
while True:
    produto = input("Informe o produto: ")
    if produto == "fim":
        break
    if produto in estoque.keys():
        qntd = int(input("Informe a quantidade: "))
        if qntd <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = qntd * preco
            print(f"{produto}: {preco:.2f} x {qntd} = {custo:.2f}\n")
            estoque[produto][0] -= qntd
            total += custo
        else:
            print("Quantidade indisponível.\n")
    else:
        print("Produto inexistente no estoque.\n")
print(f"Custo total: {total:21.2f}\n")
print("Estoque atualizado:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
