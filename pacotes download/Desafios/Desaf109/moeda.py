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
