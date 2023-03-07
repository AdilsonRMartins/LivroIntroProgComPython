from os import system, name

system("cls") if name == "nt" else system("clear")
tabuleiro_txt = """              Posições:
   |   |      7 | 8 | 9 
---+---+---  ---+---+---
   |   |      4 | 5 | 6 
---+---+---  ---+---+---
   |   |      1 | 2 | 3 
"""
posicoes = [
    None,
    (5, 1),
    (5, 5),
    (5, 9),
    (3, 1),
    (3, 5),
    (3, 9),
    (1, 1),
    (1, 5),
    (1, 9),
]
ganho = [
    [1, 2, 3],  # linha
    [4, 5, 6],
    [7, 8, 9],
    [7, 4, 1],  # coluna
    [8, 5, 2],
    [9, 6, 3],
    [7, 5, 3],  # diagonal
    [1, 5, 9]
]
tabuleiro = []
for linha in tabuleiro_txt.splitlines():
    tabuleiro.append(list(linha))

jogador = "X"
em_jogo = True
n_jogadas = 0

while True:
    for linha in tabuleiro:
        print("".join(linha))
    if not em_jogo:
        break
    if n_jogadas == 9:
        print("Deu velha!")
        break
    jogada = int(input(f"\nJogador {jogador}, digite a posição da jogada: "))
    if jogada < 1 or jogada > 9:
        print("Jogada inválida")
        continue
    if tabuleiro[posicoes[jogada][0]][posicoes[jogada][1]] != " ":
        print("\nPosição ocupada! Jogue novamente:")
        continue
    tabuleiro[posicoes[jogada][0]][posicoes[jogada][1]] = jogador
    for combinacao in ganho:
        for p_combinacao in combinacao:
            if tabuleiro[posicoes[p_combinacao][0]][posicoes[p_combinacao][1]] != jogador:
                break
        else:  # Se o for terminar sem break, todas as posicoes de p pertencem ao mesmo jogador
            print(f"\nO jogador {jogador} ganhou ({combinacao}): ")
            jogando = False
            break
    jogador = "X" if jogador == "O" else "O"
    n_jogadas += 1
