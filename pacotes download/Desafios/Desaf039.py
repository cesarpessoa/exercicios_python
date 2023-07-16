from datetime import date
'''n = str(input('informe o seu nome: ')).strip()
a = int(input('Informe o seu ano de nascimento: '))
s = str(input('informe o seu sexo: M para masculino e F para feminino. ')).strip().upper()
at = date.today().year
al = at - 18
print('Olá, {}. Seu ano de nascimento é: {}'.format(n, a))
if s == 'M':
    print('Vamos analisar sua condição para o Alistamento Militar. ')
    if a == al:
        print('Fique atento, Este ano, você completa {} anos e deve se alistar.'.format(at - al))
    elif a > al:
        print('Ainda falta(m) {} ano(s) para o seu alistamento.'. format((a - al)))
    elif a < al:
        print('Você ultrapassou o período de alistamento em {} ano(s)'.format(al - a))
else:
    print(Sendo do sexo Feminino, você não está obrigada a se alistar.
    Porém, pode escolher uma carreira e prestar concurso para as FFAA.'''

atual = date.today().year
nasc = int(input('Qual o ano de seu nascimento? '))
s = str(input('informe o ser sexo: M - Masculino e F - Feminino: ')).strip().upper()
idade = atual - nasc
al = nasc + 18
print('Quem nasceu em {} tem {} anos em {}'. format(nasc, idade, atual))
if s == 'M':
    print('Vamos analisar a sua condição para o alistamento Militar:')
    if idade == 18:
        print('Você deve se alistar IMEDIATAMENTE!')
    elif idade > 18:
        saldo = idade - 18
        print('Você deveria ter se alistado em {}. \nJá se passou(aram) {} ano(s) do prazo.'.format(al, saldo))
        print('Procure uma Junta do Serviço Militar e regularize a sua situação.')
    elif idade < 18:
        saldo = 18 - idade
        print('Você deve se alistar em {}. \nAnida falta(m) {} ano(s) para o seu alistamento.'.format(al, saldo))
else:
    print('Por ser so sexo feminino, você não precisa se alistar.')
    print('Porém, pode prestar concurso e ingressar nas FFAA.')















