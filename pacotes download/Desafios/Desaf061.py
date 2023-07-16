print('Gerador de PA!')
a1 = int(input('Digite o primeiro temo da PA: '))
r = int(input('Digite a razão da PA: '))
n = 10
termo = a1
an = 1
print('PA = ', end='')
while an <= n:
    print((termo), end=', ')
    termo += r
    an += 1
print('FIM')
