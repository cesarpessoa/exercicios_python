nome = str(input('Qual o seu nome? '))
altura = float(input('Qual a sua altura em metros? '))
peso = float(input('Qual o seu peso em Kg? '))
imc = peso / altura ** 2
print('Seu Indice de Massa Corpórea é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif 18.5 <= imc <= 25:
    print("Você esta com o peso ideal!")
elif 25 < imc <= 30:
    print('Você esta com sobrepeso')
elif 30 < imc <= 40:
    print('Você apresenta um quadro de obsidade.')
else:
    print('Você apresenta um quadro de Obesidaade Mórbida.')
print('Boa alimentação e exercícios físicos ajudam a se manter saudável!')







