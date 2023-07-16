'''Co = float(input('Digite a medida do Cateto Oposto: '))
Ca = float(input('Digite a medida do Cateto Adjacente: '))
Hi = (Co**2 + Ca**2) ** (1/2)
print('O Co mede: {}; O Ca mede: {}; logo a Hi vale: {}'.format(Co, Ca, int(Hi)))
print('O Co vale {} o Ca vale {} e a Hipotenusa {:.2f}'.format(Co, Ca, Hi))'''

'''import math
co = float(input('Mwdida do cateto oposto: '))
ca = float(input('Medida do Cateto Adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa mede: {}'.format(math.trunc(hi)))
print('A Hipotenusa vale: {:.2f}'.format(hi))'''

from math import hypot, trunc
co = float(input('Medida do Cateto Opostp: '))
ca = float(input('Medida do cateto adjacente: '))
hi = hypot(co, ca)
print('A medida da Hipotenusa é: {:.2f}'.format(hi))














