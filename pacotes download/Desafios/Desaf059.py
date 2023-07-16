from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0
while opção != 5:
    print('''Escolha uma das OPÇÕES para:
     [1] SOMAR;
     [2] MULTIPLICAR;
     [3] IDENTIFICAR O MAIOR VALOR;
     [4] DIGITAR NOVOS NÚMEROS;
     [5] ENCERRAR O PROGRAMA.''')
    opção = int(input('Digite a sua opção >>> '))
    if opção == 1:
        soma = n1 + n2
        print('A soma dos números: {} + {} = {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado da multiplicação entre {} * {} = {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            print('Entre os números {} e {}, {} é o Maior.'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre os números {} e {}, {} é o maior '.format(n1, n2, n2))
        else:
            print('Os números digitados são iguais {} = {}.'.format(n1, n2))
    elif opção == 4:
        print('Você optou por entrar com novos números:')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opção == 5:
        print('Você optou por Encerrar o programa.')
    else:
        print('Opção Inválida. Tente novamente!')
    print('=><='*20)
    sleep(2)
print('Encerrando o programa...')
sleep(1)
print('Fim!')
