def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! O valor digitado não é um número inteiro.')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número inteiro {n}.')
