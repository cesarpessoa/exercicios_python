jogo = dict()
gol = list()
partidas = list()
jogo['jogador'] = str(input('Nome: '))
part = int(input(f'Quantas partidas {jogo["jogador"]} jogou? '))
for i in range(0, part):
    gol.append(int(input(f'Quantos gols {jogo["jogador"]} fez na {i + 1}ª partida? ')))
    jogo['gols'] = gol
    tot = sum(jogo['gols'])
    jogo['total'] = tot
print('='*40)
print(jogo)
print('-'*40)
for k, v in jogo.items():
    print(f'o campo {k} tem o valor {v}')
print('='*40)
print(f'O jogador {jogo["jogador"]} jogou {len(jogo["gols"])} partidas.')
for i, g in enumerate(jogo['gols']):
    print(f'   => Na {i + 1}ª partida ele fez: {g} gol(s).')
print('='*40)
print('Programa Encerrado.')

