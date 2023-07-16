def escreva(msg):
        val = len(msg) + 4
        print('\033[34m=\033[m'*val)
        print(f'  {msg}')
        print('\033[31m=\033[m'*val)
        print()


escreva('Curso em Vídeo')
escreva('Apoie')
escreva('Vamos estudar Python')
escreva('Oi')
escreva('Mia e Maria filhas adotivas')
escreva('Sábado')


