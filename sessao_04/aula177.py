from functools import partial
from types import GeneratorType

# filter é um iterator
# filter nem sempre gera um iteravel com os mesmo tamanho da lista passada no parametro

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def filter_products(product):
    return product['preco'] > 10

products = [
    {'nome': 'Detergente', 'preco': 10.00},
    {'nome': 'Alvejante', 'preco': 22.32},
    {'nome': 'Arroz', 'preco': 50.11},
    {'nome': 'Feijão', 'preco': 20.22},
    {'nome': 'Panela', 'preco': 23.11}
]

# filtro com list comprehension
# new_produts = [p for p in products if p['preco'] > 10]

# filtro com filter e lambda (função anonima)
new_produts = filter(lambda p: p['preco'] > 10, products)

# filtro com filter e função nomeada
new_produts = filter(filter_products, products)

print_iter(products)
print_iter(new_produts)