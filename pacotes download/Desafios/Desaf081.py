num = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar[S/N]: '))
    if resp in 'Nn':
        break
print(f'foram digitados {len(num)} números.')
num.sort(reverse=True)
print(f'A lista em ordem decrescente é: {num}')
if 5 in num:
    print(f'O número 5 foi digitado na(s) posição(ões): ', end='')
else:
    print('O número 5 não foi digitado.')
for pos, c in enumerate(num):
    if c == 5:
        print(f'{pos}...', end=' ')
