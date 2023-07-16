def notas(*num, sit=False):
    r = dict()
    r['Total'] = len(num)
    r['Maior'] = max(num)
    r['Menor'] = min(num)
    r['Média'] = sum(num) / len(num)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Aprovado'
        elif r['média'] >= 5:
            r['Situação'] = 'Em Recuperação'
        else:
            r['Situação'] = 'Reprovado'
    return r


# Programa principal
resp = notas(8, 6, 10, sit=True)
print(resp)
