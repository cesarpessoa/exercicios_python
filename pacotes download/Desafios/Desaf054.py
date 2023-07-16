from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = (int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c))))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('No gupo temos: {} pessoa(s) com 21 anos ou mais'.format(maior), end='')
print(' e {} pessoa(s) menor(es) de 21 anos.'.format(menor))


