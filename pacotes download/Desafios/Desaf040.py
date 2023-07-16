a1 = float(input('Digite a sua primeira nota: '))
a2 = float(input('Digite a sua segunda nota: '))
m = (a1 + a2) / 2
print('Sua média foi {:.1f} e vocè está: '.format(m))
#m = round(m, 2)
if m < 5:
    print('\033[1;30;41m==REPROVADO==\033[m')
elif 5 <= m <= 6.9:
    print('Estude mais! Você está em \033[1;30;43m++EM RECUPERAÇÃO!!++\033[m')
else:
    print('\033[1;30;42m**PARABÉNS**!!\033[m Você foi \033[1;30;42m**APROVADO**!!\033[m')
print('Conhecimento é um bem que dura para sempre.')





