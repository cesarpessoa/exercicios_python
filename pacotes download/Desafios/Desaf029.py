vel = float(input('Qaul a velocidade do carro neste momento: '))
mul = float((vel - 80) * 7.00)
print('A velocidade máxima é de 80 Km/h')
if vel > 80:
    print("Voce ultrapassou a valocidade maxima permitida")
    print('Voce foi multado por cada KM excedente em R$ 7,00')
    print('A sua multa vai custar R$ {:.2f}'.format(mul))
    print('ATENÇÃO! Dirija con segurança')
print('Siga com segurança!')




