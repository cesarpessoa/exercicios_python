def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f


n = int(input('Digite um numero inteiro: '))
o = int(input('Digite 1 - para ver apens o fatoria e 2  - Para ver os calculos: '))
if o == 1:
    print(fatorial(n, False))
if o == 2:
    print(fatorial(n, True))
