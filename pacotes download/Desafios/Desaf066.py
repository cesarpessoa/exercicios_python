soma = cont = 0
while True:
    n = int(input('Digite um número para somar ou 999 para parar: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'\033[1;34mA soma dos {cont} números vale: {soma}\033[m')
