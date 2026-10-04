import random

jogar = 's'
while jogar == 's':
    print("\033c", end="") 
    print("######## JOGO DE ADIVINHAÇÃO ########")
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 20)")
    print("3 - Difícil (1 a 30)")

    dificuldade = int(input("Escolha a dificuldade: "))

    if dificuldade == 1:
        limite = 10
    elif dificuldade == 2:
        limite = 20
    elif dificuldade == 3:
        limite = 30
    else:
        input("Opção inválida! ENTER para tentar novamente.")
        continue

    print("\033c", end="")
    print("######## JOGO DE ADIVINHAÇÃO ########")
    print("Seja bem vindo!")
    print(f"Dê seu palpite de 1 a {limite}. Você tem 3 chances!\n")

    sorteado = random.randint(1, limite)
    for tentativa in range(1, 4):
        palpite = int(input(f"Palpite 1 de {tentativa}: "))

        if palpite == sorteado:
            print("\nParabéns, você acertou!")
            break

        if tentativa < 3:
            if palpite < sorteado:
                print("Errou! Tente um número maior!")
            else:
                print("Errou! Tente um número menor!")
        else:
            print("\nVocê perdeu! Fim de jogo!")
            print(f"O número sorteado era: {sorteado}.")

    jogar = input("Jogar novamente? (s/n): ").lower()