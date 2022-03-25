import random


def mensagem_abertura():
    print("*********************************")
    print("   Bem vindo ao jogo da forca!   ")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def oculta_palavra_secreta(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()

    return chute


def marca_chute_correto(chute, palavra_secrata_oculta, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            palavra_secrata_oculta[index] = letra
        index += 1


def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if tentativas == 6:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if tentativas == 5:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if tentativas == 4:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if tentativas == 3:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if tentativas == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if tentativas == 1:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if tentativas == 0:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def mensagem_final():
    print("*********************************")
    print("           Fim de jogo           ")
    print("*********************************")


def jogar():
    # 1 - imprimir uma mensagem de abertura do game
    mensagem_abertura()

    # 2 - carregar uma palavra do banco de dados para ser usada no game, como palavra secreta
    palavra_secreta = carrega_palavra_secreta()

    # 3 - Ocultar a palavra secreta
    palavra_secrata_oculta = oculta_palavra_secreta(palavra_secreta)

    # 4 - Mostrar a quantidade de letras da palavra secreta para jogador
    print(palavra_secrata_oculta)

    # 5 - Criar as variaveis do programa
    enforcou = False
    acertou = False
    tentativas = 7

    # 6 - Criar um laço para descobrir se jogador acertou ou não a palavra secreta
    while not acertou and not enforcou:

        # 6.1 - Pedir para o jogador chutar uma letra e guardar numa variavel
        chute = pede_chute()

        # 6.2 - Comparar se letra que jogador digitou existe na palavra secreta
        if chute in palavra_secreta:
            # 6.2.1 - Substituir a palavra secreta oculta, pelas letras que jogador acertou
            marca_chute_correto(chute, palavra_secrata_oculta, palavra_secreta)
            desenha_forca(tentativas)
        else:
            # 6.2.2 - Informar ao jogador que ele errou e atualizar o numero de tentativas
            tentativas -= 1
            desenha_forca(tentativas)

        # 6.3 - Verificar se o jogardor acertou ou não a palavra
        enforcou = tentativas == 0
        acertou = "_" not in palavra_secrata_oculta
        print(palavra_secrata_oculta)

    # 7 - imprimir uma mensagem que o jogador venceu o game
    if acertou:
        mensagem_vencedor()

    # 8 - imprimir uma mensagem que o jogador perdeu o game
    else:
        mensagem_perdedor(palavra_secreta)

    # 9 - imprimir uma mensagem de fim de jogo
    mensagem_final()


if __name__ == "__main__":
    jogar()
