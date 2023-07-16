def metade(n):
    res = n / 2
    return res


def dobro(n):
    res = n * 2
    return res


def moeda(n=0, moeda='R$'):
    return f'{moeda} {n:>6.2f}'.replace('.', ',')


def aumento(n, taxa):
    res = n + (n * taxa / 100)
    return res


def desconto(n, taxa):
    res = n - (n * taxa / 100)
    return res
