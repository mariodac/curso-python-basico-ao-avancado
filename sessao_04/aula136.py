# List comprehension em Python
# List comprehension é uma forma rápida para criar listas 
# a partir de iteráveis.

print(list(range(10)))

lista = [
    number * 2
    for number in range(10)
]

print(lista)