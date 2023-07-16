n = int(input('Digite um número e veja a sua tabuada de multiplicar: '))
for c in range(1, 11, 1):
    p = n * c
    #print('{:2} * {} = {:2}'.format(c, n, p))
    print('{:2} * {} = {:2}'.format(c, n, c * n))
print('Fim')



