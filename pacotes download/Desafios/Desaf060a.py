from time import sleep
n = int(input('Disgite um número para obrer o seu Fatorial: '))
c = n
f = 1
print('\033[1;34mProcessando...\033[m')
sleep(1)
print('\033[1;34mO Fatorial de {}!\033[m = '.format(n), end='')
for c in range(n, 0, -1):
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '=', end='')
    f *= n
    n -= 1
#sleep(1)
print(' \033[1;34m{}\033[m'.format(f))
