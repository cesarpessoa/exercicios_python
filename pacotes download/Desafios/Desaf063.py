print('Sequência de Fibonacci: \033[1;34m(0 - 1 - 1 - 2 - 3 - 5 - 8 -...)\033[m')
n = int(input('Quntos termos você deseja ver? '))
t1 = 0
t2 = 1
cont = 3
print('{} > {}'.format(t1, t2), end=' ')
while cont <= n:
    t3 = t1 + t2
    print('> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim.')
