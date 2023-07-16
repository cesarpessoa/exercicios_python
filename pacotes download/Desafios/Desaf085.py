núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
núm[0].sort()
núm[1].sort()
print('='*30)
print(f'Lista Completa: {núm}.')
print(f'Números pares {núm[0]}.')
print(f'Números ímpares: {núm[1]}')
print('='*30)

