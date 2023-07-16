num = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um número: '))
    num.append(n)
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
num.sort()
par.sort()
impar.sort()
print(f'A lista completa é: {num}')
print(f'Os números pares são: {par}')
print(f'os números impares são: {impar}')

