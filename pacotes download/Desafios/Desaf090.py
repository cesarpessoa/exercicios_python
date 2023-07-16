Aluno = dict()
Aluno['Nome'] = (str(input('Digite o nome do aluno: ')))
Aluno['Média'] = (float(input(f'Digite a Média de {Aluno["Nome"]}: ')))
print('='*30)
if Aluno['Média'] >= 7:
    Aluno['Situação'] = '\033[1:34mAprovado!\033[m'
elif 5 < Aluno['Média'] < 7:
    Aluno['Situação'] = '\033[1;33mEm Recuperação\033[m!'
else:
    Aluno['Situação'] = '\033[1;31mReprovado!\033[m'
print('Resultado Final:')
for k, v in Aluno.items():
    print(f'{k} é igual a: {v}')
print('='*30)
