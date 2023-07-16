from time import sleep
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
print('Vou comparar qual é o maior entre eles..')
print('=' * 14)
print('PROCESSANDO...')
print('=' * 14)
sleep(2)
if n1 > n2:
    print('O primeiro número foi {} e ele é o maior.'.format(n1))
elif n2 > n1:
    print('O segundo número foi {} e ele é o maior.'.format(n2))
else:
    print('Os números são iguais.')
