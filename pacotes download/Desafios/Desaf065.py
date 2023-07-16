resp = 'S'
cont = s = média = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    s += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S / N] ')).upper().strip()[0]
média = s / cont
print('Você digitou {} números e a média foi {:.2f}.'.format(cont, média))
print('O MAIOR valor foi {} e o MENOR foi {}.'.format(maior, menor))
print('Fim')

