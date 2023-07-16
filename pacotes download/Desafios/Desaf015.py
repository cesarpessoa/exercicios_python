d = int(input('Por quantos dias o carro ficou alugado? '))
k = float(input('Quantos quilomentos ele rodou? '))
# print('Dias de locação: {}; \n Quilometragem: {:.0f} Km'.format(d, k))
lc = d * 60.00 + k * 0.15
print('O custo final da locaçãoe é de R$ {:.2f}'.format(lc))




