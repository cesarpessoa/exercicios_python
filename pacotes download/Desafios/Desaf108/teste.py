from Desaf108 import moeda

p = float(input('Digite um valor R$ '))
print(f'A metade do valor {moeda.moeda(p)}; vale: {moeda.moeda(moeda.metade(p))}')
print(f'O dobro do valor {moeda.moeda(p)}; vale: {moeda.moeda(moeda.dobro(p))}')
print(f'+ 10% no valor {moeda.moeda(p)}; temos: {moeda.moeda(moeda.aumento(p, 10))}')
print(f'- 5% no valor {moeda.moeda(p)}; temos: {moeda.moeda(moeda.desconto(p, 5))}')
