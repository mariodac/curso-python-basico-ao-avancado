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
pessoa = {
    'nome': 'Mario',
    'sobrenome': 'Cabral',
    # 'idade': 900,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
print('quantidades de chaves', len(pessoa))
print('chaves', list(pessoa.keys()))
print('valores', list(pessoa.values()))
print('chaves e valores',list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)