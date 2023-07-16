n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
print('Analisando os números digitados: {}, {} e {}.'.format(n1, n2, n3))
if n1 == n2 and n2 == n3:
    print('Os numeros digitados são iguais.')
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi: {}'.format(menor))
print("O maior valor digitado foi: {}".format(maior))
















