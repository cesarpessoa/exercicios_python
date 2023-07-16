def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[34mErro! Existe um problema com o tipo de dados digirado.\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário decidiu interromper o programa.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[34mErro! Por favor, digite um número Real.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'O usuario optou por não continuar.')
            return 0
        else:
            return n
