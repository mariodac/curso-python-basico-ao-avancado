# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy
d1 = {
    'nome': 'Mario',
    'sobrenome': 'Cabral',
    'enderecos': [0, 1, 2, 3, 4, 5],
}

d2 = copy.deepcopy(d1)
d2['nome'] = 1000
d1['enderecos'][0] = 1
print(d1)
print(d2)