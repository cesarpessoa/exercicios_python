D = float(input('Quanatos Km até o seu destino? '))
print('O Valor por Km é R$ 0,50 até 200Km e R$ 0,45 para percursos superiores.')
if D <= 200:
    print('O valor de sua passagem é: R$ {:.2f}'.format(D * 0.50))
else:
    print('O Valor de sua passagem é: R$ {:.2f}'.format(D * 0.45))
print('Boa Viagem')





