from Desaf109 import moeda

p = float(input('Digite um valor R$ '))
print(f'A metade do valor {moeda.moeda(p)}; vale: {moeda.metade(p, True)}')
print(f'O dobro do valor {moeda.moeda(p)}; vale: {moeda.dobro(p, True)}')
print(f'+ 10% no valor {moeda.moeda(p)}; temos: {moeda.aumento(p, 10, True)}')
print(f'- 5% no valor {moeda.moeda(p)}; temos: {moeda.desconto(p, 5, True)}')
