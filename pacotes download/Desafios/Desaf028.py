from random import randint
from time import sleep
n = randint(0, 5)  # 'Faz o Computador escolher um número'
n2 = int(input('Descubra qual número inteiro, entre 0 e 5, o computador vai escolher?  '))
print('...VERIFICANDO DADO DIGITADO COM O ESCOLHIDO...')
sleep(2)
print('O computador escolheu: {}'.format(n))
print('E você escolheu: {}'.format(n2))
if n == n2:
    print('PARABENS, você acertou')
else:
    print('Você errou')
if n == n2:
    print('---FIM---')
else:
    print('Tente outra vez!')










