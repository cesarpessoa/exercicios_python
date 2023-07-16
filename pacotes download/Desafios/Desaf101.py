def votação(nome, ano):
    from datetime import date # Uma forma de economizar memoria uso so na funcão
    idade = date.today().year - ano
    if 18 <= idade <= 65:
        return f'{nome}, você tem {idade} anos. ' \
               f'\033[1;31mSeu voto é Obrigatório!\033[m'
    elif 16 <= idade < 18:
        return f'{nome}, você tem {idade} anos. ' \
               f'\033[1;33mSeu voto é Facultativo!\033[m'
    else:
        return f'{nome}, você tem {idade}, anos. ' \
               f'\033[1;32mVocê está dispensado e não precisa votar!\033[m'


n = str(input('Digite o seu nome: '))
a = int(input('Digite a sua idade: '))
votação(n, a)
print('='*40)
print(votação(n, a))
print('='*40)
