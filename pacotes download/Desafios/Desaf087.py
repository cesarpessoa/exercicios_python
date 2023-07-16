matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = maior = scol3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite uma valor para posição: [{l}, {c}]: '))
print('='*30)
print(f'{"MATRIZ 3 X 3":^20}')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
    print()
print('='*30)
print(f'A soma dos elementos pares da Matriz vale: {sp}')
for l in range(0, 3):
    scol3 += matriz[l][2]
print(f'A soma dos elementos da 3ª coluna vale: {scol3}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior elemento da 2ª linha é o número: {maior}')
