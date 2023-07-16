s = float(input('Qual o valor do seu salário em R$ '))
print("O valor informado foi R$ {:.2f}".format(s))
if s <= 1250.00:
    print('Seu novo salário será: R$ {:.2f}'.format(s * 1.15))
    print('Seu reajuste foi de R$ {:.2f}'.format(s * 0.15))
else:
    print('Seu novo salário será: R$ {:.2f}'.format(s * 1.10))
    print('Seu reajuste salarial foi de R$ {:.2f}'.format(s * 0.10))



