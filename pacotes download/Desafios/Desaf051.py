a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = int(input('Digite a ordem do termo an: '))
an = a1 + r * (n - 1)
print('Os temps da PA são:')
for c in range(a1, an + 1, r):
    print('{}'.format(c), end=" ")
print('\nO {}º termo da PA de razão r = {} e A1 = {} é: A{} = {}. '.format(n, r, a1, n, an))

