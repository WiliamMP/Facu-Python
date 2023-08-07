import random

print('Eu escolhi minha jogada, escolha a sua humano imbecil')

print('Menu de opções: \n')

# dar as opções para usuário escolher
print('[1] PEDRA \n')
print('[2] PAPEL \n')
print('[3] TESOURA \n')
print('[4] NENHUM \n')

# pega valor aleatório

Lista_Valores = ('PEDRA', 'PAPEL', 'TESOURA', 'NENHUM')

def jogar_pedra_papel_tesoura():
    jogada_bot = random.choice(Lista_Valores)
    valor_entrada = input('Faça sua jogada: \n')

    while jogada_bot == 'NENHUM':
        jogada_bot = random.choice(Lista_Valores)

    jogada_player = Lista_Valores[int(valor_entrada)-1] 

    if (jogada_bot == 'PEDRA' and jogada_player == 'TESOURA'):
        print('Jogo ganhou \n')
    if (jogada_bot == 'PEDRA' and jogada_player == 'PAPEL'):
        print('Jogador ganhou \n')
    if (jogada_bot == 'PEDRA' and jogada_player == 'PEDRA'):
        print('Houve empate \n')
        jogar_pedra_papel_tesoura()

    if (jogada_bot == 'PAPEL' and jogada_player == 'PEDRA'):
        print('Jogo ganhou \n')
    if (jogada_bot == 'PAPEL' and jogada_player == 'PAPEL'):
        print('Houve empate \n')
        jogar_pedra_papel_tesoura()
    if(jogada_bot == 'PAPEL' and jogada_player == 'TESOURA'):
        print('Jogador ganhou \n')

    if(jogada_bot == 'TESOURA' and jogada_player == 'PEDRA'):
        print('Jogo ganhou \n')
    if(jogada_bot == 'TESOURA' and jogada_player == 'PAPEL'):
        print('Jogador ganhou \n')
    if(jogada_bot == 'TESOURA' and jogada_player == 'TESOURA'):
        print('Houve empate \n')
        jogar_pedra_papel_tesoura()


    if(jogada_player == 'NENHUM'):
        print('Jogador covarde, desistiu do jogo')

    if(jogada_bot == 'NENHUM'):
        print('Jogo covarde, desistiu do jogo')
    
    print(f'Resultado = Jogada do jogo {jogada_bot} vs Jogada do player {jogada_player}')


jogar_pedra_papel_tesoura()


     