import forca
import adivinhacao

print("*********************************")
print("       Escolha o seu jogo!       ")
print("*********************************")

print("""[1] Adivinhação 
[2] forca""")

jogar = True

while jogar:

    jogo = int(input("Qual jogo deseja jogar? "))

    if jogo == 1:
        print()
        adivinhacao.jogar()
        jogar = False
    elif jogo == 2:
        print()
        forca.jogar()
        jogar = False
    else:
        print("Opção inválida")
        continue
