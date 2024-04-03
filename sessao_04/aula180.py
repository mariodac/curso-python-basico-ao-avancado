# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base para a recursão
# - fatorial - n! = 5! =   * 4 * 3 * 2 * 1 = 120
# python tem o limite de 1000 iterações de call stack
import sys
# excede o limite de call stack
sys.setrecursionlimit(1004)
def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(1000))