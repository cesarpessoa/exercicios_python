'''num = int(input('Digite um número entre 0 e 9999: '))
n = str(num)
print('O número digirado foi: {} e ele possui:'.format(num))
print('{} unidades'.format(n[3]))
print('{} dezenas'.format(n[2]))
print('{} centenas'.format(n[1]))
print('{} milhar'.format(n[0]))'''
num = int(input('Digite um número: '))
print('O número digitado foi: {} e ele possui:'.format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('{} unidades'.format(u))
print('{} dezenas'.format(d))
print('{} centenas'.format(c))
print('{} milhar(es)'.format(m))















