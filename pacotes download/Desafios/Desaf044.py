p = float(input('Qual o preço do produto em R$ '))
print('''FORMAS DE PAGAMENTO:
0 - A vista, com 10% de desconto; 
1 - 1 vez no cartão com 5% de desconto; 
2 - 2 vezes no cartão preço normal.; 
3 - 3 vezes ou mais no cartão com 20% de acréscimo.''')
f = int(input('escolha na lista acima como você quer pagar: '))
pa = p - (p * 0.10)
pc1 = p - (p * 0.05)
pc2 = p
pc3 = p + (p * 0.20)
#print(pa, pc1, pc2, pc3)
if f == 0:
    print('Comprando a vista você vai pagar R$ {:.2f} pelo produto.'.format(pa))
if f == 1:
    print('Comprando em 1 vez no cartão o produto vai custar R$ {:.2f}.'.format(pc1))
if f == 2:
    print('Em até 2 vezes no cartão você paga o preço nominal R$ {:.2f}.'.format(pc2))
    print('Você vai pagar 2 parcelas de R$ {:.2f}.'.format(pc2 / 2))
if f == 3:
    print('Comprando em 3 vezes, você vai pagar R$ {:.2f}'.format(pc3))
    n = int(input('Em quantas parcelas você quer pagar? '))
    print('Você vai pagar {} parcelas de R$ {:.2f}.'.format(n, pc3 / n))
print('Obrigado por escolher nossa loja. Volte Sempre!!')













