'''import math
num = float(input('Digite um número decimal: '))
print('O número digitado foi: {} e sua parte inteira é: {}'.format(num, math.trunc(num)))'''
from math import trunc
num = float(input('Digite um número decimal: '))
#print('O número digitado foi: {}; sua parte inteira é {}'.format(num, trunc(num)))
print('O numero digitado foi: {} e sua parte inteira é: {}'.format(num, int(num)))





