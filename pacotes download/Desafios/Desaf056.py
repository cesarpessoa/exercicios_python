somaidade = médiaidade = maioridade = mulher20 = 0
nomevelho = ""
for p in range(1, 5):
    print('------ {} PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo [M / F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {:.2f} anos.'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'. format(maioridade, nomevelho))
print('O total de mulheres com menos de 20 anos é: {}'.format(mulher20))



