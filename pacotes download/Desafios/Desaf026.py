frase = str(input('Digite uma frase: ')).lower().strip()
#frase = frase.lower()
print('A letra A aparece {} na frase'.format(frase.count('a')))
print('A primeira letra A aparece na posição: {}'.format(frase.find('a') + 1))
print('A ultima letra A aparece na posição: {}'.format(frase.rfind('a') + 1))

