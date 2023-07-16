def metade(n, formato=False):
    """
    => Função Metade de um número
    :param n: Recebe valor informado pelo usuário
    :param formato: Opcional para mostrar formato de moeda R$
    :return: O valor de n / 2
    """
    res = n / 2
    return res if not formato else moeda(res)


def dobro(n, formato=False):
    """
    => Calcula o dobro de um valor informado
    :param n: Recebe o valor a ser cálculado o dobro
    :param formato: opcional para mostrar o valor de moeda R$
    :return: Retorna o dobro do valor informado formatado ou não.
    """
    res = n * 2
    return res if not formato else moeda(res)


def aumento(n, taxa, formato=False):
    """
    => Cálcula o aumento aplicando a taxa informada
    :param n: Valor que se quer aumentar
    :param taxa: Percentual de aumento nro. int sobre n
    :param formato: opcional, para exibir formato em moeda R$
    :return: Retorna o valor n acrecido da taxa
    """
    res = n + (n * taxa / 100)
    return res if not formato else moeda(res)


def desconto(n, taxa, formato=False):
    """
    => Cálculo de desconto sobre o valor n baseado na taxar
    :param n: Valor que se quer aplicar o desconto
    :param taxa: Taxa de desconto percentual nro. int a ser aplicada sobre n
    :param formato: opcional para exibir o formato em moeda R$
    :return: Retorna o valor de n abatido o desconto relativo a taxar
    """
    res = n - (n * taxa / 100)
    return res if not formato else moeda(res)


def moeda(n=0, moeda='R$'):
    """
    => Aplicando simbolo monetário R$ e substitui ponto por virgula na impressão
    :param n: Valor informado pelo usuário
    :param moeda: insere o simbolo R$ ante o valor n
    :return: Retorna o valor n com o simbolo monetário
    """
    return f'{moeda} {n:>6.2f}'.replace('.', ',')


def resumo(n=0, taxaa=10, taxar=15):
    """
    => Função Resumo para impressão e organização dos dados
    :param n: Valor informado pelo usuário
    :param taxaa: nro. int para cálculor aumento sobre n
    :param taxar: nro. int para cálculor desconto sobre n
    :return: Retorna resumo das funções metade, dobro, aumento e desconto em quadro organizado.
    """
    print('='*40)
    print('Resumo do Valor'.center(30))
    print('='*40)
    print(f'Preço Analisado: \t\t{moeda(n)}')
    print(f'A metade do preço: \t\t{metade(n, True)}')
    print(f'O dobro do preço: \t\t{dobro(n, True)}')
    print(f'+ {taxaa}% o preço ficou: \t{aumento(n, taxaa, True)}')
    print(f'- {taxar}% o preço ficou: \t{desconto(n, taxar, True)}')
    print('='*40)

