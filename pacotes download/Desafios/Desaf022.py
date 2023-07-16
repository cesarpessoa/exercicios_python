frase = str(input('Digite o seu nome: ')).strip()
print('Analisando seu nome: {}'.format(frase))
print('Seu nome em maiusculas é: {}'.format(frase.upper()))
print('Seu nome em minusculas é: {}'.format(frase.lower()))
print('Seu nome tem {} caracteres.'.format(len(frase) - frase.count(' ')))
# print('Seu primeiro nome tem {} letras.'.format(frase.find(' ')))
separa = frase.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))





