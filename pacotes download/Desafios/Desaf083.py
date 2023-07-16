exp = str(input('Digite uma expressão matemática com parenteses: '))
mat = list()
for simb in exp:
    if simb == '(':
        mat.append('(')
    elif simb == ')':
        if len(mat) > 0:
            mat.pop()
        else:
            mat.append(')')
            break
if len(mat) == 0:
    print('A expressão está válida.')
else:
    print('Verifique o fechamento dos parenteses. Expressão inválida.'





)