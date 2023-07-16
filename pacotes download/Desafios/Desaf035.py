print("Digite o comprimento de três resta, e veja se formam um triangulo")
r1 = float(input('Comprimento de r1 em cm = '))
r2 = float(input('Comprimento de r2 em cm = '))
r3 = float(input('Comprimento de r3 em cm = '))
if (r1 + r2) < r3 or (r1 + r3) < r2 or (r2 + r3) < r1 or r1 == r2 == r3:
    print("Estas três restas formam um Triangulo.")
else:
    print('Não é possível formar um triangulo con estas restas.')


