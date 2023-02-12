from os import system, name

system("cls") if name == "nt" else system("clear")
último = 0
fila1 = []
fila2 = []
while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1, e {len(fila2)} clientes na fila 2")
    print(f"Fila 1 atual: {fila1}")
    print(f"Fila 2 atual: {fila2}")
    print("Digite F para adicionar um cliente ao fim da fila 1, G para fila 2")
    print("ou A para realizar o atendimento da fila 1 ou B para fila 2. S para sair.")
    operação = input("Operação (F, G, A, B ou S):").upper()
    ordem = 0
    sair = False
    while len(operação) > ordem:
        if operação[ordem] == "A" or operação[ordem] == "F":
            fila = fila1
        else:
            fila = fila2
        if operação[ordem] == "A" or operação[ordem] == "B":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação[ordem] == "F" or operação[ordem] == "G":
            último += 1  # Incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[ordem] == "S":
            sair = True
            break
        else:
            print("Operação inválida! Digite apenas F, G, A, B ou S!")
        ordem += 1
    if sair:
        break
