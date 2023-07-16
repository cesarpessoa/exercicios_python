def área(l, c):
    print('-'*20)
    a = l * c
    if l != c and l != 0 and c != 0:
        print(f"A área do terreno com medidaas {l} m por {c} m, vale: {a} m².")
    if l == 0 or c == 0:
        print('Impossível calcular área com medida igual a zero.')
    if l == c and l != 0 and c != 0:
        print(f'As medidadas {l} e {c}, não formam um terreno retangular.')


l = (int(input(f'Digite a largurado em metros do terreno: ')))
c = (int(input(f'Digite o comprimento em metros do terreno: ')))
área(l, c)
