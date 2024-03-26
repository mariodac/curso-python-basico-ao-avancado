"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

=================== resultado 
lista_soma = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = []

# Solução generica
range_min = 1
if len(lista_a) > len(lista_b):
    range_min = len(lista_b)
else:
    range_min = len(lista_a)
for i in range(range_min):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

# Solução pythonica I
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

# Solução pythonica II
from itertools import zip_longest
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=10)]
print(lista_soma)