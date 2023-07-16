print('''Digite vários números interios. 
Para parar e ver a qauntidde e a soma, digite 999.''')
n = soma = cont = 0
n = int(input('Digite um numero inteiro: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número inteiro: '))
print('Você digitou {} números, cuja soma vale: {}.'.format(cont, soma))
