iten = ('Café', 15.00, 'Açúcar', 8.00, 'Água', 3.00, 'Carne', 110.00)
print('='*40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('='*40)
for c in range(0, len(iten)):
    if c % 2 == 0:
        print(f'\n{iten[c]:.<30}', end='')
    else:
        print(f'R$ {iten[c]:>6.2f}')


