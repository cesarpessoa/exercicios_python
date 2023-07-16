from random import randint
núm = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram: ', end=' ')
for n in núm:
    print(f'{n}', end=' ')
print(f'\nO menor valor sorteado foi: {min(núm)}')
print(f'O maior valor sorteado foi: {max(núm)}')

maior = sorted(núm)
print(f'O menor número sorteado foi {maior[0]}')
print(f'O maior número sorteado foi {maior[-1]}')
print(maior)


