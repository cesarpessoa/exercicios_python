c = ('\033[m', # 0 - Sem cores
     '\033[0;29;41m', # 1 - Vermelho
     '\033[0;30;42m', # 2 - Verde
     '\033[0;30;43m', # 3 - Amarelo
     '\033[0;30;44m', # 4 - Ciano
     '\033[0;30;47m', # 5 - Roxo
     '\033[0;29m', # 6 Branco
 );


def ajuda(com):
    título(f'Acessando o manual de comando \'{com}\'', 4)
    print(c[5], end="")
    help(com)
    print(c[0], end='')


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(c[0], end="")


# Programa principal
comando = ''
while True:
    título('Sistema de Ajuda PyHelp', 1)
    comando = str(input('Função ou Biblioteca:> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até logo!', 1)
