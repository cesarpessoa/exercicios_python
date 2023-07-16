n = int(input('Digite um número: '))
div = 0
print('DIVISORES DE {}:'.format(n))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', end=' ')
        div += 1
    else:
        print('\033[34m', end=' ')
    #print('{}'.format(c), end=' ')
print('\n\033[mO número {} possui {} divisor(es).'.format(n, div))
if div == 2:
    print('E por isso ele é \033[32mPRIMO.\033[m')
else:
    print('E por isso ele \033[1;31mNÃO é PRIMO.\033[m')




