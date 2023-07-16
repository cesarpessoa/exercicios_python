from time import sleep


def lin():
    print('\033[1;34m=\033[m'*43)


def contador(i, f, p):
    lin()
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'Contagem dos números de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
            sleep(0.5)
        print('Fim.')
        lin()
        print()
    if i > f:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
            sleep(0.5)
        print('Fim')
        lin()


i = 0
f = 10
p = 1
contador(i, f, p)
i = 10
f = 0
p = 2
contador(i, f, p)
print('Agora é a sua vez. Defina:')

i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
