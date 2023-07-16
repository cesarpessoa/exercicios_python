from random import randint
from time import sleep

print('Sorteando 5 números....')
sleep(2)


def sorteia(lista):
    for cont in range(0, 5):
        n = randint(0, 10)
        numeros.append(n)
        print(f'{n}', end=" ")
    print('Fim!')
    sleep(1)


def somaPar(lista):
    soma = cont = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
            cont += 1
    print(f'\033[34m\nEntre os números sorteados {cont} é(são) par(es) e a soma vale: {soma}\033[m')


numeros = []
sorteia(numeros)
somaPar(numeros)