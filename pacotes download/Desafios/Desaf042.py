print('=' * 25)
print('Analisador de Triangulos!')
print('=' * 25)
'''r1 = float(input('Digite o valor de R1: '))
r2 = float(input('Digite o valor de r2: '))
r3 = float(input('Digite o valor de r3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima formam um triangulo.')
    if r1 != r2 and r1 != r3 and r2 != r3:
        print("Elas formam um triangulo Escaleno")
    if r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print('Elas formam um triangulo Isosceles')
    if r1 == r2 == r3:
        print('Elas formam um triangulo Equilatero')
else:
    print('Os segmentos acima NÃO podem formar um triangulo.')
#print('Nem sempre três regras formam um triangulo.')'''
r1 = float(input('Digite o valor de r1: '))
r2 = float(input('Digite o valor de r2: '))
r3 = float(input('Digite o valor de r3: '))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos de reta FORMAM UM TRIANGULO: ', end="")
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('Estes segmentos de reta NÃO FORMAM UM TRIANGULO!')





