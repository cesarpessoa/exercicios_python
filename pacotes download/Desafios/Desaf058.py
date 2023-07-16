from random import randint
c = randint(0, 10)
#print(c)
print('\033[1;31m****** JOGO DA ADVINHAÇÃO ******\033[m')
print('\033[1;34mO computador já escolheu um número entre 0 e 10.\033[m')
j = int(input('Tente descobrir. Qual a sua resposta? '))
t = 1
while j != c:
    j = int(input('Tente outra vez: '))
    t += 1
    if j == c:
        print('\033[1;33mParabéns!!!\033[m')
    else:
        if j > c:
            print('Menos... ')
        elif j < c:
            print('Mais...')
print('Após {} tentativa(s), você \033[1;34mACERTOU!!!\033[m'.format(t))


