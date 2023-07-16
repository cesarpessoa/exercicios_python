import os
from time import sleep
from random import randint
from operator import itemgetter
print(f'{">>>>> JOGANDO >>>>> DADOS<<<<<":^40}')
print()
sleep(1)
ranking = list()
while True:
    apostas = {'jogador1': randint(1, 6),
               'jogador2': randint(1, 6),
               'jogador3': randint(1, 6),
               'jogador4': randint(1, 6)}

    for k, v in apostas.items():
        print(f'O {k} jogou o dado e tirou {v} pontos.')
        sleep(1)
    print('><'*20)
    print(f'{"CLASSIFICÇÃO DOS JOGADORES":^40}')
    sleep(1)
    ranking = sorted(apostas.items(), key=itemgetter(1), reverse=True)
    for i, k in enumerate(ranking):
        print(f'O {i + 1}º colocado foi o {k[0]} com {k[1]} pontos. ')
        sleep(1)
    opc = str(input('Quer fazer nova jogada? [S/N]: ')).upper()[0]
    for opc in 'SN':
        if opc in 'S':
            apostas = {'jogador1': randint(1, 6),
                        'jogador2': randint(1, 6),
                        'jogador3': randint(1, 6),
                        'jogador4': randint(1, 6)}
    else:
        break
print('Fim de Jogo')
