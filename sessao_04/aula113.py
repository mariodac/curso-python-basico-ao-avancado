# Exercícios com funções

# Crie uma função que multiplica todos os argumentos # não nomeados recebidos
# Retorne o total para uma variável e mostre o valor # da variável.

# Crie uma função fala se um número é par ou ímpar. # Retorne se o número é par ou impar.
# Retorne se o número é par ou impar
import random

def multiplicacao(*numeros):
    total = 1
    for numero in numeros:
        total *= numero
    return total
    
def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'PAR'
    return 'IMPAR'
    
numero = random.randint(1, 100)
resultado = par_ou_impar(numero)
print(f'{numero} é {resultado}')
outro_resultado = multiplicacao(1, 2 ,3, 4, 5)
print(f'A multiplicação é igual {outro_resultado}')
    