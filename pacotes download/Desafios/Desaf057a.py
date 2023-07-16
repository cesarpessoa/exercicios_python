sexo = str(input('Digite seu sexo: [M / F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Opção inválida. Digite o seus sexo: [M/F]: ')).upper().strip()[0]
print('Sexo [{}] digitado com sucesso.'.format(sexo))
