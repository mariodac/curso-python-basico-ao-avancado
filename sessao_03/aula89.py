"""
enumerate - enumera iteraveis (indices)
"""

lista = ['Maria', 'Helena', 'Luiz', 'Mario', 'Douglas']
lista_enumerada = list(enumerate(lista))
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla')
    for valor in tupla_enumerada:
        print(f'\t{valor}')