from time import sleep


def maior(*num):
    print('\033[1;34m=\033[m'*40)
    cont = maior = 0
    print('Analisando os números... ')
    sleep(0.5)
    for n in num:
        print(f'{n}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print()
    print(f'Foram analisados {cont} números e o maior é {maior}')
    print('\033[1;34m=\033[m' * 40)
    print()
    sleep(0.5)


maior(8, 5, 3, 6, 1)
maior(2, 0)
maior(2)
maior(5, 1, 3, 9, 0)
maior()