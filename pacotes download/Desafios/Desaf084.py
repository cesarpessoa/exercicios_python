lista = []
dados = []
cont = maior = menor = 0
while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))
    dados.append(nome)
    dados.append(peso)
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]: '))
    cont += 1
    if resp in 'Nn':
        break
print(f'Foi(ram) cadastrada(s) {cont} pessoa(s).')
print(f'O menor peso registrado foi de {menor} kilos. Que pertence a: ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O maior peso registrado foi de {maior} kilos. Que pertence a: ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
