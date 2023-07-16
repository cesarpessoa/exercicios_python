from time import sleep
import emoji
from random import choice
print('Vamos jogar Jo Quem Pô? ')
r = 'pedra'
p = 'papel'
t = 'tesoura'

Lista = [r, p, t]
c = choice(Lista).lower()

print('O Computador já escolheu. Agora é a sua vez: ')
j = str(input('Então, o que você escolhe: pedra, papel ou tesoura? ')).strip().lower()

print('\033[7;31;40mJO\033[m')
print(emoji.emojize('\033[1;33m:punch:\033[m', language='alias'))
sleep(0.5)
print('\033[7;32;40mKEN\033[m')
print(emoji.emojize('\033[1;33m:hand:\033[m', language='alias'))
sleep(0.5)
print('\033[7;36;40mPÔ\033[m')
print(emoji.emojize('\033[1;33m:v:\033[m', language='alias'))
if c == r and j == t or c == t and j == p or c == p and j == r:
    print('\033[1;29;41mO COMPUTADOR escolheu {} e VENCEU!\033[m. Tente outra vez'.format(c))
elif j == r and c == t or j == t and c == p or j == p and c == r:
    print('O computador escolheu {} e \033[7;32;40mVOCÊ VENCEU!\033[m!'.format(c))
elif c == j:
    print('\033[1;29;40mVocês empataram, o computador escolheu {} também.\033[m'.format(c))
else:
    print('\033[7;29;40mOpção INVÁLIDA! tente novamente.\033[m')



















