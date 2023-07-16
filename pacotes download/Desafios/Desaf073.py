brasil = ('Corinthians', 'Santos', 'América-MG', 'Bragantino', 'São Paulo',
               'Atlético-MG', 'Botafogo', 'Internacional', 'Coritiba', 'Avaí',
               'Cuiabá', 'Athlético-PR', 'Palmeiras', 'Flamengo', 'Fluminense',
               'Goiás', 'Ceará SC', 'Juventude', 'Atlético-GO', 'Fortaleza')
print('=-'*40)
print(f'Classificação do Brasileirão 2022: {brasil}')
print('><'*40)
print(f'\033[1;32mOs 5 primeiros colocados são:\033[1;34m{brasil[0:5]}\033[m')
print('><'*40)
print(f'\033[1;31mOs 4 times na zona de rebaixamento são:\033[1;34m{brasil[-4:]}\033[m')
print('><'*40)
print(f'\033[1;36mA lista em ordem Alfabetica é: {sorted(brasil)}\033[m')
print('><'*40)
print(f'\033[1;34mO Bragantino está na {brasil.index("Bragantino") + 1}ª posição.\033[m')
print('=-'*40)
while True:
        while True:
            cla = str(input('Digite o nome do seu time e descubra a classificação: '))
            if cla in brasil:
                    break
            print(f'\033[1;33mVerifique se o time consta na tabela e a grafia do nome.\033[m')
        print(f'\033[1:34mO {cla} está na {brasil.index(cla) + 1}ª posição\033[m')
        op = str(input('Quer consultar outro time? [S/N]: ')).upper().strip()[0]
        while op not in 'SN':
            op = str(input('Quer consultar outro time? [S/N]: ')).upper().strip()[0]
        if op in 'N':
            break
print('\033[1;31mPrograma encerrado.\033[m')


