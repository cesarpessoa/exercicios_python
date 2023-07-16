'''import random
Pri = str(input('Primeiro nome: '))
seg = str(input('Segundo nome: '))
ter = str(input('Terceiro nome: '))
Quar = str(input('Quarto nome: '))
Lista = [Pri, seg, ter, Quar]
random.shuffle(Lista)
print('A ordem dos alunos é: {} ')
print(Lista)'''

from random import shuffle
a1 = str(input('Primeiro Aluno: '))
a2 = str((input('Segindo aluno: ')))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação é: ')
print(lista)












