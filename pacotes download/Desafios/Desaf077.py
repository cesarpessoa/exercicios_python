palavras = ('Aprender', 'Mercado', 'Curso', 'Teoria')
print(palavras)
for c in palavras:
    print(f'\nNa palavra {c.upper()}, temos:', end=' ')
    for l in c:
        if l in 'AaEeIiOoUu':
            print(f'{l.lower()}', end=' ')

