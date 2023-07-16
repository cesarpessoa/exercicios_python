from time import sleep
times = []
jogo = dict()
gol = list()
gols = list()
partidas = list()
while True:
    jogo.clear()
    jogo['jogador'] = str(input('Nome: '))
    part = int(input(f'Quantas partidas {jogo["jogador"]} jogou? '))
    gol.clear()
    for i in range(0, part):
        gol.append(int(input(f'Quantos gols {jogo["jogador"]} fez na {i + 1}ª partida? ')))
    for c in gol:
        print('', end='')
        jogo['gols'] = gol[:]
        jogo['total'] = sum(gol)
    times.append(jogo.copy())
    while True:
        opc = str(input('Quer Continuar? [S/N]: ')).upper()[0]
        if opc in 'SN':
            break
        print('Atenção. Digite apenas S ou N.')
    if opc == 'N':
        break
print('='*40)
print('Nro ', end='')
for i in jogo.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(times):
    print(f'{k:<3}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
while True:
    dados = int(input(f'De qual jogador você deseja ver os dados? (999 para parar): '))
    if dados == 999:
        break
    if dados >= len(times):
        print(f'  Atenção!! O Nro. {dados} não está na lista.')
    else:
        print(f' DADOS DO JOGADOR: {times[dados]["jogador"]}')
        for i, g in enumerate(times[dados]['gols']):
            print(f'Na {i + 1}ª partida {times[dados]["jogador"]} fez {g} gols.')
        print('='*40)
print('\033[1:34mPrograma Encerrado!\033[m')

