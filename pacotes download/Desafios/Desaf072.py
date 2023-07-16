cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
       'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
       while True:
              núm = int(input('Digite um número entre 0 e 20: '))
              if 0 <= núm <= 20:
                     break
              print('Tente novamente. ', end='')
       print(f'Você digitou o número {núm} - {cont[núm]}')
       op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
       while op not in 'SN':
              op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
       if op in 'N':
              break
print('Programa Encerrado.')










