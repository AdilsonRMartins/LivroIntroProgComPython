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
numero = int(input("Informe um número: "))
indice = (numero * 776) % len(palavra)

for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra[indice]:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra[indice]:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra[indice]:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros >= 4:
        linha2 = " \|/ "
    print(f"X{linha2}")
    linha3 = ""
    if erros == 5:
        linha3 += " /   "
    elif erros >= 6:
        linha3 += " / \ "
    print(f"X{linha3}")
    print("X\n===========")
    if erros == 6:
        print(f"A palavra sercreta é: {palavra[indice]}")
        print("Enforcado!")
        break
