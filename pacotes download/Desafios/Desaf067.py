while True:
    print('\033[1;34m       Tabuada de um Número!\033[m')
    n = int(input('''Digite um número positivo para ver a sua Tabuada 
ou um número negativo para parar:  '''))
    print(f'\033[1;32mTABUADA DE {n}.\033[m')
    print('='*14)
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c:2} = {n*c:3}')
    print('='*14)
print('\033[1;33mVocê optou par encerrar o programa TABUADA.\033[m')

