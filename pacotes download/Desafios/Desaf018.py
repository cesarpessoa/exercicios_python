'''import math
an = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(an))
print('O seno de {}º é: {:.2f} '.format(an, sen))
cosr = math.cos(math.radians(an))
print('O coseno de {}º e: {:.2f} '.format(an, cosr))
tang = math.tan(math.radians(an))
print('A tangente de {}º é: {:.2f}'.format(an, tang))'''

from math import cos, sin, tan, radians

angulo = float(input('Digite a medida de um ângulo em graus: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print('O ângulo de {:.0f}º tem seno igual a: {:.2f} coseno {:.2f} e'.format(angulo, seno, coss))
print('Tangente {:.2f}'.format(tang))





