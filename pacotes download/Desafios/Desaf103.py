def ficha(nome='Desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gols')


# prograna Principal
n = str(input('Digite o nome: '))
g = str(input('Quantos gols marcou: '))
print()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
