a = int(input('Digite um ano: '))
print('Analisando o ano de: {}'.format(a))
if a % 4 == 0:
    if a % 100 != 0:
        print('Este ano é Bisexto')
    else:
        if (a % 400) != 0:
            print('Este ano não é Bisexto')
        else:
            print('Este ano é Bisexto.')
else:
    print("Este ano não é Bisexto")


