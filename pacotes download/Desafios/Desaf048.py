soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma = soma + num # ou soma += num
        cont += 1 # cont = cont + 1
print('A soma dos números, entre 1 e 500, que são multiplos de 3 é: {}'.format(soma))
print('Neste intervalo existem {} números.'.format(cont))
print('fim')


