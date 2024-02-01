# Manipulando chaves e valores em dicionarios
pessoa = {
    'nome': 'Mário',
    'sobrenome': 'Cabral',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
chave = 'nome'
pessoa[chave] = 'Mário'
pessoa['sobrenome'] = 'Cabral'
lista = []

print(pessoa)
pessoa[chave] = 'Paulo'

del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is not None:
    print(pessoa['sobrenome'])
else:
    print('não existe')
