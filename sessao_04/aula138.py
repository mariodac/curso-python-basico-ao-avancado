# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# Mapeamento de dados em list comprehension

import pprint

def pretty_print(arg):
    pprint.pprint(arg, sort_dicts=False, width=40)
products = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

new_products = [
    {**product, 'preco': product['preco'] * 1.05}
    if product['preco'] > 20 else {**product}
    for product in products
    if product['preco'] > 10
]

# print(*new_products, sep='\n')

pretty_print(new_products)


lista = [
    n
    for n in range(10)
    if n < 5
]
print(lista)