# Dictionary Comprehension e Set Comprehension
product = {
    'nome': 'Caneta Azul',
    'preco' : 2.5,
    'categoria': 'Escritório',
}

# dc = {
#     key: value
#     if isinstance(value, (int, float)) else value.upper()
#     for key, value in product.items()
#     if key != 'categoria'
# }

dc = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value in product.items()
    if key != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]
new_list = dict(lista)
dc = {
    key: value
    for key, value in lista
}

print(dc)

s1 = {i ** 2 for i in range(10)}
print(s1)