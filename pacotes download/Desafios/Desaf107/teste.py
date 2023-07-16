from Desaf107 import moeda

p = float(input('Digite um valor R$ '))
print(f'A metade do valor R$ {p} vale: R$ {moeda.metade(p)}')
print(f'O dobro do valor R$ {p} vale: R$ {moeda.dobro(p)}')
print(f'+ 10% no valor {p}, temos: R$ {moeda.aumento(p, 10)}')
print(f'- 5% no valor {p}, temos: R$ {moeda.desconto(p, 5)}')
