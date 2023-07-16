def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Existe um problema com o tipo de dados digirado.\033[m')
            continue
        except KeyboardInterrupt:
            print('O usuário decidiu interromper o programa.')
            return 0
        else:
            return n


def linha(tam=42):
    return '=' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
        cont += 1
    print(linha())
    opc = leiaInt('\033[32mDigite sua opção: \033[m')
    return opc


