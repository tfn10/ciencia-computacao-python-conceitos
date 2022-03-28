"""No jogo NIM n peças são inicialmente dispostas numa mesa ou tabuleiro.
Dois jogadores jogam alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças
possíveis ganha o jogo."""


def computador_escolhe_jogada(n, m):
    pass


def usuario_escolhe_jogada(n, m):
    while True:
        usuario_retira = int(input('Quantas peças você vai tirar? '))
        print()
        if 0 < usuario_retira < m:
            break
        print('Oops! Jogada inválida! Tente de novo.\n')
    return usuario_retira


def partida():
    print('Bem-vindo ao jogo do NIM! Escolha:\n')
    tipo_partida = int(input('1 - para jogar uma partida isolada\n'
                             '2 - para jogar um campeonato '))

    if tipo_partida == 1:
        print('Voce escolheu um campeonato!')
    elif tipo_partida == 2:
        print('Voce escolheu uma partida isolada!')


def campeonato():
    for rodada in range(1, 4):
        print(f'**** Rodada {rodada} ****\n')
        quantidade_pecas = int(input('Quantas peças? '))
        limite_pecas = int(input('Limite de peças por jogada? '))
        print()
        voce_joga = quantidade_pecas % (limite_pecas + 1) == 0

        if voce_joga:
            print('Voce começa!')
        else:
            print('Computador começa!')

        pecas_restantes = quantidade_pecas
        while True:
            if voce_joga:
                pecas_retiradas = usuario_escolhe_jogada(pecas_restantes, limite_pecas)
                pecas_restantes -= pecas_retiradas
            else:
                pecas_retiradas = computador_escolhe_jogada(quantidade_pecas, limite_pecas)
                pecas_restantes -= pecas_retiradas
            if pecas_restantes == 0:
                break