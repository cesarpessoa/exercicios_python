primeiro = int(input('Digite o primeiro termno da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
print('Termos da PA: ', end=' ')
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=', ')
        termo += razão
        cont += 1
    print('PAUSA...')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('Foram calculados {} termos nesta PA. '.format(total))

