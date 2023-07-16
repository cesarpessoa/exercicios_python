n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Os números digitados foram: {n}')
print(f'O número 9 foi digitado {n.count(9)} vez(es).')
if 3 in n:
    print(f'O número 3 foi digitado pela primeira vez na {n.index(3) + 1}ª posição.')
else:
    print(f'O número 3 não foi digitado.')
for p in n:
    if p % 2 == 0:
        print(f'{p} ', end=' ')
print(f'São números PAR: ', end='')
#else:
    #print('Não foram digitados números PAR.')


