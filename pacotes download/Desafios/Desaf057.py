sexo = 'FM'
while sexo == sexo:
    sexo = str(input('''Digite o seu sexo:
    [M] - Masculino
    [F] - Feminino: 
    >>: ''')).upper().strip()[0] #Fatiamento checa apenas a primeira letra digitada
    if sexo in 'Mm Ff':
        print('Opção registrada com sucesso.')
    else:
        print('oção inválida, tente novamente:')
