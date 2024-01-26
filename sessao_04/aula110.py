"""
Retorno de valores das funções (return)
args - Argumentos não nomeados
* 0 *args (empacotamento e desempacotamento)
"""


def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y

def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    print(total)


# variavel = soma(1, 2)
# variavel = int('1')
multiplicacao(1, 2, 3, 4)
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))