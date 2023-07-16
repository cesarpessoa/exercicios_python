n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para Conversão:
[1] - Converter para BINÁRIO
[2] - Converter para OCTAL 
[3] - Converter para HEXADECIMAL''')
b = int(input('Escolha uma das opções de base na lista acima: '))
if b == 1:
    print('{} convertido para BINÁRIO é igual a: {}'.format(n, bin(n)[2:]))
elif b == 2:
    print('{} convertido para OCTAL é igual a: {}'.format(n, oct(n)[2:]))
elif b == 3:
    print('{} convertido para HEXADECIMAL é igual a: {}'.format(n, hex(n)[2:]))
else:
    print('Opção Invalida! Consulte a lista e tente novamente.')




