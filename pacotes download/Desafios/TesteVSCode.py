compras = []

while True:

    opcao = input(f'Escolha uma das opções:\
(i)nserir, (a)pagar, (l)istar, (s)air: ').lower().strip()
    if opcao not in 'ials':
        print('Opção invalida. Escolha apenas (i, a, l ou s).')
        continue

    if opcao == 'i':
        item = input('Digite o nome do produto: ').title().strip()
        compras.append(item)
    if opcao == 'a':
        e = input(f'Digite o número do\
item a ser excluido ou 0 (zero) para continuar: ').strip()
        e = int(e)
        if e >= 1:
            del compras[e - 1]
        elif e == 0:
            continue

    if opcao == 'l':
        for indice, nome in enumerate(compras, start=1):
            print(indice, nome)
    if opcao == 's':
        break

print('Você optou por sair do programa.')
