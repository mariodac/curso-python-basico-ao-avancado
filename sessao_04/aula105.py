"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
parametros está na definição da função
os argumentos são os valores passados na chamada da função
"""

def imprimir(a, b, c):
    print('Hello World!')
    print('Hello, Python Devs')

imprimir(1, 2, 3)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Mario')
saudacao()