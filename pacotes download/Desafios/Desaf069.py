maior18 = homens = mmenos20 = 0
cont = 1
while True:
    print('Quer caadastrar uma pessoa?')
    print('='*30)
    idade = int(input('DIGITE A IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('DIGITE O SEXO [M/F]: ')).upper().strip()[0]
    if idade > 18:
        maior18 += 1
    if sexo in 'Mm':
        homens += 1
    if idade < 20 and sexo in 'F':
        mmenos20 += 1
    print('='*30)
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar: [S/N]: ')).upper().strip()[0]
    if esc in 'Nn':
        break
    cont += 1
print(f'''Foram cadastradas {cont} pessoas. 
Analisando os dados temos:
{maior18} pessoa(s) com mais de 18 anos.
{homens} São Homens e
{mmenos20} Mulher(es) com menos de 20 anos.''')

