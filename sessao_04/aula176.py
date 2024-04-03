from functools import partial
from types import GeneratorType

# map pode alterar os dados e gera uma iteravel do mesmo tamanho da lista passado no parametro
# map é um iterator, por isso ocorre o esgostamento, para evitar esgotamento realizar a coerção
# partial funciona como o closure


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def increase_percentage(value, percentage):
    return round(value * percentage, 2)

def change_product_price(product):
    return {**product, 'preco': increase_10_percentage(product['preco'])}

products = [
    {'nome': 'Detergente', 'preco': 10.00},
    {'nome': 'Alvejante', 'preco': 22.32},
    {'nome': 'Arroz', 'preco': 50.11},
    {'nome': 'Feijão', 'preco': 20.22},
    {'nome': 'Panela', 'preco': 23.11}
]

increase_10_percentage = partial(increase_percentage, percentage=1.1)

# mapeamento com list comprehension
# new_products = [ {**p, 'preco': increase_10_percentage( p['preco'])} for p in products]
new_products = map(change_product_price, products)

products_generator = (x for x in products)
print(isinstance(products_generator, GeneratorType))

print_iter(products)
print_iter(new_products)