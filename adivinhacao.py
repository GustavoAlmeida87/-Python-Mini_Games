import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    tentativa = 1
    pontos = 1000

    print("Qual nível de dificuldade gostaria de jogar!")
    print("""[1] - Fácil 
    [2] - Normal
    [3] - Dífícil""")

    while tentativas == 0:

        nivel = int(input("Defina o nível de dificuldade: "))

        if nivel == 1:
            tentativas = 15
        elif nivel == 2:
            tentativas = 10
        elif nivel == 3:
            tentativas = 5
        else:
            print("Opção inválida")
            continue

    while tentativa <= tentativas:

        print(f"Tentativa {tentativa} de {tentativas}")

        numero_digitado = int(input("Digite o seu número entre 1 e 100: "))

        if (numero_digitado > 100) or (numero_digitado < 1):
            print("Número inválido, digite um número entre 1 e 100")
            continue

        print("Você digitou:", numero_digitado)

        acertou = numero_digitado == numero_secreto
        maior = numero_digitado > numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        elif maior:
            print("Você errou! O seu número foi maior do que o número secreto.")
            pontos -= abs(numero_secreto - numero_digitado)
            tentativa += 1
        else:
            print("Você errou! O seu número foi menor do que o número secreto.")
            pontos -= abs(numero_secreto - numero_digitado)
            tentativa += 1

    print("*********************************")
    print("           Fim de jogo           ")
    print("*********************************")


if __name__ == "__main__":
    jogar()
