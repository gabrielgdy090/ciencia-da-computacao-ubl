def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    elif (n % (m + 1)) == 0:
        return m
    else:
        return n % (m + 1)

def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada <= 0 or jogada > m or jogada > n:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada <= 0 or jogada > m or jogada > n:
            print("Jogada inválida! Tente novamente.")
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("Você começa!")
        vez_do_usuario = True
    else:
        print("Computador começa!")
        vez_do_usuario = False

    while n > 0:
        if vez_do_usuario:
            jogada = usuario_escolhe_jogada(n, m)
            print("Você tirou", jogada, "peça(s).")
        else:
            jogada = computador_escolhe_jogada(n, m)
            print("O computador tirou", jogada, "peça(s).")

        n -= jogada
        print("Agora restam", n, "peça(s) no tabuleiro.\n")

        vez_do_usuario = not vez_do_usuario

    if vez_do_usuario:
        print("O computador ganhou!")
        return False
    else:
        print("Você ganhou!")
        return True

def campeonato():
    placar_usuario = 0
    placar_computador = 0
    for _ in range(3):
        if partida():
            placar_usuario += 1
        else:
            placar_computador += 1
    print("Placar: Você", placar_usuario, "X", placar_computador, "Computador")

def main():
    print("Bem-vindo ao jogo NIM!\n")
    print("Escolha uma opção:")
    print("1 - Jogar uma partida")
    print("2 - Jogar um campeonato")

    opcao = int(input())

    if opcao == 1:
        print("\nPartida simples:")
        partida()
    elif opcao == 2:
        print("\nCampeonato:")
        campeonato()
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()
