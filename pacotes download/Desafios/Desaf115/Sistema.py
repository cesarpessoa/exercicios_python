from Desaf115.lib.interface import *
from Desaf115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Listar Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        # Opção de listar o contúdo de um arquivo
        lerArquivo(arq)
    elif resp == 2:
        # Opção de adicionar um item a um arquivo
        cabeçalho('Novo Cadastro')
        nome = str(input('Digite o Nome: '))
        idade = leiaInt('Digite a Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do Sistema...')
        break
    else:
        cabeçalho('\033[31mErro! Digite de acordo com o Menu.\033[m')
    sleep(2)

