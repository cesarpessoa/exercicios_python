from random import randint
import emoji
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print('O Computador escolheu: {}. '.format(itens[computador]))
print('''Suas Opcções:
[0] - Pedra
[1] - Papel
[2] - Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print(emoji.emojize(':punch: JO', language='alias'))
sleep(0.5)
print(emoji.emojize(':hand: QUEM', language='alias'))
sleep(0.5)
print(emoji.emojize(':v: PÔ', language='alias'))
sleep(0.5)
print('>='*12)
print('O Computador jogou {} '.format(itens[computador]))
print('O Jogador jogou {} '.format(itens[jogador]))
print('<='*12)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('VOCÊS EMPATARAM!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('VOCÊS EMPATARAM!')
    elif jogador ==2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('VOCÊS ENPATARAM!')
    else:
        print('JOGADA INVÁLIDA')







