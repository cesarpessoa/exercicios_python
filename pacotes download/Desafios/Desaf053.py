frase = str(input('Escreva uma frase e verifique se é um PALIÍNDROMO: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#print('Você digitou a frase: {}'.format(junto))
#print(len(junto), junto)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
    #print(junto[letra], end='')
if junto == inverso:
    print('A frase ou palavra: \033[1;33m{} \033[1;34mé um PALÍNDROMO.\033[m'.format(frase))
    print('\033[1;34m{} = {}\033[m'.format(junto, inverso))
else:
    print('A frase ou palavra: \033[1;33m{} \033[1;31mNÃO É UM PALÍNDROMO.\033[m'.format(frase))
    print('\033[1;31m{} != {}\033[m'.format(junto, inverso))








