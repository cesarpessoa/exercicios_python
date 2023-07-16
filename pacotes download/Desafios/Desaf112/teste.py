from Desaf112.utilidadescev import moeda
from Desaf112.utilidadescev import dado
from Desaf112.utilidadescev.moeda import metade, dobro, aumento, desconto

p = dado.leiadinheiro('Digite um valor R$ ')
print('='*40)
moeda.resumo(p, 5, 10)

print(help(aumento))


