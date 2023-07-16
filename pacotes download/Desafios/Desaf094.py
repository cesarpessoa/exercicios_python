cadastro = []
pessoas = dict()
média = list()
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [F/M]: ')).upper()[0]
        if pessoas['sexo'] in 'FM':
            break
        print('Atenção! Digite apenas F = Feminino ou M = Masculino.')
    pessoas['idade'] = int(input('idade: '))
    cadastro.append(pessoas.copy())
    média.append(pessoas['idade'])
    mgrupo = sum(média) / len(média)
    while True:
        opc = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if opc in 'SN':
            break
        print('Por favor. Digite apenas Sim ou Não: [S/N]!')
    if opc == 'N':
        break
print('='*40)
print(f'A - Temos {len(cadastro)} pessoa(s) cadastrada(s)')
print(f'B - A média de idade do Grupo é: {mgrupo:5.2f} anos.')
print('C - As mulheres cadastradas foram: ', end=' ')
for m in cadastro:
    if m['sexo'] == 'F':
        print(f'{m["nome"]}', end=' ')
print()
print(f'D - As pessoas com idade superior a média do grupo são:')
for c in cadastro:
    if c['idade'] > mgrupo:
        print('', end='')
        for k, v in c.items():
            print(f' => {k} = {v};', end=' ')
        print()
print('='*40)
print('Programa Encerrado')



