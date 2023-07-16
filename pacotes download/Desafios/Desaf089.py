boletim = list()

while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], média])
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('*'*30)
print(f'{"Nro.":<4}  {"Nome":<10}  {"Média":>4}')

for i, a in enumerate(boletim):
    print(f'{i:^4}  {a[0]:<10}  {a[2]:>4.1f}')
print('*'*30)
while True:
    opc = int(input('De qual aluno deseja ver as notas. (Digite 999 para parar): '))
    if opc == 999:
        break
    if opc <= len(boletim) - 1:
        print(f'As notas de {boletim[opc][0]} foram: {boletim[opc][1]}')
print('Programa encerrado.')
