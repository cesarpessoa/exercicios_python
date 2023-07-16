lista = []
for c in range(0, 5):
    #n = int(input(f'Digite um valor para posição {c}: '))
    #lista.append(n)
    lista.append(int(input(f'Digite um número para posição {c}: ')))
    #Forma simplificada

print('<>'*20)
print(f'Vocé digitou os valores: {lista}')
print(f'O menor valor digitado foi {min(lista)}, na(s) posição(ôes): ', end='')
for pos, v in enumerate(lista):
    if v == min(lista):
        print(f' {pos + 1}...', end=' ')
print(f'\nO maior valor digitado foi {max(lista)}, na(s) posição(ões): ', end='')
for pos, v in enumerate(lista):
    if v == max(lista):
        print(f' {pos +1}...', end=' ')
print('\nFim.')
