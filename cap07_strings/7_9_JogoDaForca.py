from os import system, name

system("cls") if name == "nt" else system("clear")
palavra = ["abissal",
           "amigo",
           "animal",
           "ano",
           "bacante",
           "banheiro",
           "bicho",
           "bisonho",
           "bola",
           "cabelo",
           "cachorro",
           "cacofonia",
           "cama",
           "carro",
           "casa",
           "celular",
           "cidade",
           "computador",
           "cor",
           "coração",
           "criatura",
           "daimon",
           "dia",
           "ectoplasma",
           "escola",
           "escrupuloso",
           "estrada",
           "estrela",
           "fantasma",
           "festa",
           "flor",
           "fogo",
           "frio",
           "furtivo",
           "garoto",
           "gato",
           "gosto",
           "igreja",
           "jabuti",
           "janela",
           "jardim",
           "jardim",
           "jogo",
           "jubiloso",
           "liturgia",
           "livro",
           "lugar",
           "mesa",
           "museu",
           "narcisismo",
           "noite",
           "nome",
           "objeto",
           "ocultismo",
           "olho",
           "papel",
           "parque",
           "pessimismo",
           "pessoa",
           "pessoal",
           "piloto",
           "pintura",
           "planta",
           "ponto",
           "porta",
           "pouco",
           "praia",
           "prato",
           "professor",
           "quadro",
           "quimera",
           "quotidiano",
           "rabugice",
           "raiz",
           "rio",
           "roupa",
           "rua",
           "sala",
           "sapato",
           "sarcasticamente",
           "sinal",
           "sofisma",
           "sol",
           "som",
           "sombra",
           "somente",
           "sorriso",
           "sorvete",
           "tambor"
           "telefone",
           "telhado"
           "tempo",
           "teto",
           "tijolo",
           "tinta",
           "tio",
           "trabalho",
           "travessura",
           "trem",
           "tremulante",
           "trono",
           "ultrajante",
           "vento",
           "viagem",
           "vida",
           "vigoroso",
           "voraz",
           "voz",
           "ziguezagueante",
           "acrimonioso",
           "amor"]
indice = int(input("Digite um numero:"))
palavra = palavra[(indice * 776) % len(palavra)]
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0

linhas_txt = """
X==:==
X  :
X    
X    
X    
X    
=======

"""

linhas = []

for linha in linhas_txt.splitlines():
    linhas.append(list(linha))

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
            if erros == 1:
                linhas[3][3] = "O"
            elif erros == 2:
                linhas[4][3] = "|"
            elif erros == 3:
                linhas[4][2] = "\\"
            elif erros == 4:
                linhas[4][4] = "/"
            elif erros == 5:
                linhas[5][2] = "/"
            elif erros == 6:
                linhas[5][4] = "\\"
    for l in linhas:
        print("".join(l))
    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break
