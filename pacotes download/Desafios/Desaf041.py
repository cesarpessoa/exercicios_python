'''from datetime import date
n = str(input('Informe o seu nome: '))
a = int(input("Qaual o seu ano de nascimento? "))
at = date.today().year
if a >= (at - 9):
    print('Olá, {}. Você faz parte da categoria Mirim.'. format(n))
elif a < (at - 9) and a >= (at - 14):
    print('Olá, {}. Vocè faz parte da categoria infantil.'.format(n))
elif a < (at - 14) and a >= (at - 19):
    print('Olá, {}. Vocè faz parte da categoria Junior.'.format(n))
elif a == (at - 20):
    print('Olá, {}. Você faz parte da categoria Senior'.format(n))
#elif a <= (at - 20):
else:
    print('Olá, {}. Você faz parte da categoria Master.'.format(n))
2013 a 2022 - Mirim
2008 a 2012 - Infantil
2003 a 2007 - Junior
2002 - 2002 - Senior
Antes - 2002 - Master'''

from datetime import date
atual = date.today().year
nome = str(input('Qual o seu nome? '))
nascimento = int(input('Em que ano você nasceu? '))
idade = atual - nascimento
print('Olá, {}. Você tem {} anos.'.format(nome, idade))
if idade <= 9:
    print('Você pertence a categoria MIRIM.')
elif idade <= 14:
    print('Você pertence a categoria INFANTIL.')
elif idade <= 19:
    print('Você pertence a categoria JUNIOR.')
elif idade <= 25:
    print('Você pertence a categoria SÊNIOR.')
else:
    print('Você pertence a categoria MASTER.')
print('Tenha uma vida saudável com boa alimentação e prática esportiva.')



