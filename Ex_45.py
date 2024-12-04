from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 14)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 14)
if computador == 0: # computador jogou Pedra
    if jogador == 0:
        print('Empate!!!')
    elif jogador == 1:
        print('Jogador Venceu!!')
    elif jogador == 2:
        print('Computador Venceu!!!')
    else:
        print('Jogada Inválida')
elif computador == 1: # computador jogou Papel
    if jogador == 0:
        print('Computador Venceu!!!')
    elif jogador == 1:
        print('Empate!!!')
    elif jogador == 2:
        print('Jogador Venceu!!!')
    else:
        print('Jogada Inválida')
elif computador == 2: # computador jogou Tesoura
    if jogador == 0:
        print('Jogador Venceu!!!')
    elif jogador == 1:
        print('Computador Venceu')
    elif jogador == 2:
        print('Empate!!!')
    else:
        print('Jogada Inválida')





