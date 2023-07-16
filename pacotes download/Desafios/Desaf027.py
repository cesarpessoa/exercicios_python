n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print(len(nome))
print('Olá, {}. Prazer em conhecer.'.format(n))
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))
print('Seu nome é composto de {} partes'.format(len(nome)))








