from os import system, name

system("cls") if name == "nt" else system("clear")
último = 10
fila = list(range(1, último + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação (F, A ou S):").upper()
    ordem = 0
    sair = False
    while len(operação) > ordem:
        if operação[ordem] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação[ordem] == "F":
            último += 1  # Incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[ordem] == "S":
            sair = True
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        ordem += 1
    if sair:
        break
