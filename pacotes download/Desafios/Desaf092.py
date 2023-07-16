from datetime import date
from time import sleep
cad = dict()
cad['Nome'] = str(input('Nome: '))
cad['Nasc'] = int(input('Ano de nascimento: '))
cad['CTPS'] = int(input('CTPS nro.: '))
if cad['CTPS'] == 0:
    for k, v in cad.items():
        print(f'{k} = {v}')
if cad['CTPS'] > 0:
        idade = date.today().year - cad['Nasc']
        cad['Idade'] = idade
        cad['Contrato'] = int(input('Ano de contratação '))
        cad['Salario R$'] = float(input('Salário em R$: '))
        aposente = f'{(cad["Contrato"] - cad["Nasc"] + 35)} anos'
        cad['Aposentadoria com'] = aposente
        print('='*20)
        for k, v in cad.items():
            print(f'{k}:  {v}')
            sleep(1)
print('='*20)
print('Programa Encerrado!')
