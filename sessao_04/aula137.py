# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
list_numbers = []
for numero in range(10):
    list_numbers.append(numero)
# print(lista)
    
list_numbers = [
    numero * 2
    for numero in range(10)
]
# print(list_numbers)

# Mapeamento de dados em list comprehension
products = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

new_products = [
    {**product, 'preco': product['preco'] * 1.05}
    if product['preco'] > 20 else {**product}
    for product in products
]

print(*new_products, sep='\n')

