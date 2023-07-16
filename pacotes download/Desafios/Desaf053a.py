frase = str(input('Escreva uma frase e verifique se é um PALÍNDROMO: ')).strip().upper()
palavras= frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(palavras, junto, inverso)
print('O inverso de: {} é: {}'.format(junto, inverso))
if junto == inverso:
    print('TEMOS UM PALÍNDROMO: \033[1;34m{} = {}.\033[m'.format(junto, inverso))
else:
    print('\033[1;34m{} \033[me \033[1;31m{}\033[m, NÃO FORMAM PALÍNDROMO'.format(junto, inverso))

