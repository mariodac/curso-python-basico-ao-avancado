# reduce - faz a redução de um iterável em um valor
# reduce retorna um acumulador e um item da lista por padrão
# sempre passar valor inicial para evitar problema
from functools import reduce

products = [
    {'nome': 'Detergente', 'preco': 10.00},
    {'nome': 'Alvejante', 'preco': 22.32},
    {'nome': 'Arroz', 'preco': 50.11},
    {'nome': 'Feijão', 'preco': 20.22},
    {'nome': 'Panela', 'preco': 23.11}
]

def sum_product(accumulator, product):
    return accumulator + product['preco']

# realizando soma de todos os preços de produto com loop
# total = 0
# for p in products:
#     total += p['preco']

# realizando soma de todos os preços de produto com SUM
print(sum([p['preco'] for p in products]))

# realizando soma de todos os preços de produto com reduce e função nomeada
total = reduce(sum_product, products, 0)

# realizando soma de todos os preços de produto com reduce e função anonima
total = reduce(lambda ac, p: ac + p['preco'], products, 0)
print(total)