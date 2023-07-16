def metade(n, formato=False):
    res = n / 2
    return res if not formato else moeda(res)


def dobro(n, formato=False):
    res = n * 2
    return res if not formato else moeda(res)


def aumento(n, taxa, formato=False):
    res = n + (n * taxa / 100)
    return res if not formato else moeda(res)


def desconto(n, taxa, formato=False):
    res = n - (n * taxa / 100)
    return res if not formato else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda} {n:>6.2f}'.replace('.', ',')


def resumo(n=0, taxaa=10, taxar=15):
    print('='*40)
    print('Resumo do Valor'.center(30))
    print('='*40)
    print(f'Preço Analisado: \t\t{moeda(n)}')
    print(f'Ametade do preço: \t\t{metade(n, True)}')
    print(f'O dobro do preço: \t\t{dobro(n, True)}')
    print(f'+ {taxaa}% o preço ficou: \t{aumento(n, taxaa, True)}')
    print(f'- {taxar}% o preço ficou: \t{desconto(n, taxar, True)}')
    print('='*40)

