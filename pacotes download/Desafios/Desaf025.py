'''nome = str(input('Digite o seu nome completo: '))
nome = 'SILVA' in nome.upper()
print('Em seu nome tem a palavra Silva? {}'.format(nome))'''

nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome tem a palavra Silva? {}'.format('silva' in nome.lower()))

