# Combinations Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*iterator, sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Mario'
]

camisetas = [
    ['preta', 'azul'],
    ['P', 'M', 'G'],
    ['MASCULINO', 'FEMININO'],
    ['ALGODÃO', 'POLIESTER'],
    ['adult', 'infantil']

]
print('COMBINAÇÃO')
print_iter(combinations(pessoas, 2))
print('PERMUTAÇÃO')
print_iter(permutations(pessoas, 3))
print('PRODUTO')
print_iter(product(*camisetas))
