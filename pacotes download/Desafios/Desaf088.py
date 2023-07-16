from random import randint
from time import sleep
aposta = list()
jogos = []
print()
print(f'{"APOSTANDO NA MEGA SENA":^40}')
print()
q = int(input(f'Quantos jogos você deseja fazer: '))
total = 1
while total <= q:
    cont = 0
    while True:
        núm = randint(1, 60)
        if núm not in aposta:
            aposta.append(núm)
            cont += 1
        if cont >= 6:
            break
    aposta.sort()
    jogos.append(aposta[:])
    aposta.clear()
    total += 1
print(f'{"PROCESSANDO...":^30}')
sleep(1)
print('>><<'*9)
for i, l in enumerate(jogos):
    print(f' {i + 1}º jogo: {l}')
    print('.'*35)
    sleep(1)



