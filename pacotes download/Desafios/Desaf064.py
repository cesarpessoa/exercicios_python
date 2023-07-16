print('''       Digite quantos números inteiros você quiser.
Digite 999 (flag) para parar, contar e somar os números digitados.''')
n = cont = s = total = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
    cont += 1
    total = cont - 1
print('Você digitou {} e a soma deles é igual a : {}'. format(total, s - 999))
