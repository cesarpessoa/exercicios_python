num = list()
for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if cont == 0 or n > num[-1]:
        num.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < num[-1]:
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Adicionado à lista na posição {pos}')
                break
            pos += 1
print(f'Lista dos números digitados:{num}')
