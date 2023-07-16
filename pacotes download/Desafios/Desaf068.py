cont = 0
from random import randint
while True:
    c = randint(0, 5)
    print(c)
    j = int(input('Escolha um número entre 0 e 5: '))
    esc = str(input("Você escolhe Par (P) ou Impar (I): ")).upper().strip()[0]
    if (c + j) % 2 == 0 and esc in 'P':
        print(f'O PC escolheu {c} e você escolheu {j}. {c + j} é PAR e Võce venceu!!')
    if (c + j) % 2 == 1 and esc in 'I':
        print(f'O PC escolheu {c} e você escolheu {j}. {c + j} é IMPAR e Você venceu!!')
    elif (c + j) % 2 == 0 and esc in 'I' or (c + j) % 2 == 1 and esc in 'P':
        break
    cont += 1
print(f'\033[1;031mGAME OVER!!!\033[m Você acertou {cont} vez(es).')



