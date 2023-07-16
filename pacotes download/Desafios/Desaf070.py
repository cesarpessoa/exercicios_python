tot = vlmaismil = cont = menor = 0
barato = ' '
print('LOJA DO POVO.')
while True:
    prod = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor R$ '))
    tot = tot + valor
    cont += 1
    if valor > 1000:
        vlmaismil += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = prod
    ad = ' '
    while ad not in 'SN':
        ad = str(input('Quer adcionar outro produto? [S/N]: ')).upper().strip()[0]
    if ad in 'N':
        break
print(f'O Valor total da compra foi R$ {tot:.2f}')
print(f'{vlmaismil} produto(s) com valor acima de R$ 1.000,00')
print(f'O Produto mais barato é o(a) {barato} e custa R$ {menor:.2f}')

