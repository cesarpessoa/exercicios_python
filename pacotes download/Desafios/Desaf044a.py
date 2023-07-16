print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Qual o valor de sua compras em  R$ '))
print('''FORMAS DE PAGAMENTO:
[1] À vista, dinheiro ou cheque,
[2] À vista no Cartão de Crédito
[3] Em 2 vezes no Cartão de Crédito
[4] Em 3 vezes ou mais no Cartão de Crédito.
 ''')
opção = int(input('Qual a sua opção de pagamento? '))
if opção == 1:
    total = preço - (preço * 0.10)
    print('Comprando à vista no dinheiro ou cheque, você vai pargar R$ {:.2f}'.format(total))
elif opção == 2:
    total = preço - (preço * 0.05)
    print('Em 1 vez no cartão de crédito você vai pagar {:.2f}'.format(total))
elif opção == 3:
    total = preço
    parcela = preço / 2
    print('Em 2 vezes no cartão você vai pagar R$ {:.2f} em 2 parcelas de R$ {:.2f}'.format(total, parcela))
    print('Sem juros')
elif opção == 4:
    total = preço + (preço * 0.20)
    n = int(input('Em quantas parcelas você quer pagar? '))
    parcela = total / n
    if n >= 3:
            print('Você decidiu dividir em 3 vezes ou mais.')
            print('O valor total será de R$ {:.2f} em {} parcelas de R$ {:.2f} '. format(total, n, parcela))
            print('Com juros')
    else:
        print('Para esta opção, o úmero de parcelas deve ser igual ou maior que três!')
else:
    print('Opção INVÁLIDA!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preço, total))






