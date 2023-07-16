valor = float(input('Qual o valor do imóvel que você pretende comprar? R$ '))
renda = float(input('Qual o valor de sua Renda atual? R$ '))
tempo = int(input('Em quantos anos você pretende pagar? '))
p = valor / (tempo * 12)
if p <= (renda * 0.30):
    print('Parabnés!! Seu financiamento foi \033[7;29;40mAPROVADO\033[m.')
    print('O imovel custa R$ {:.2f} \nSua renda é R$ {:.2f} \nPara o prazo de {} anos:'.format(valor, renda, tempo))
    print('O Valor de sua prestação mensal será R$ {:.2f}'.format(p))
else:
    print('Infelizmente seu financiamento foi \033[1;30;41mNEGADO\033[m.')
    print('O valor da prestação ultrapassa 30% da sua renda mensal.')









