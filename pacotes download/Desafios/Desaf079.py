lista = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, não será adicionado. ')
    r = str(input('Quer continuar? [S/N]: '))
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
lista.sort()
print(f'A lista dos valores em ordem crescente é: {lista}')


