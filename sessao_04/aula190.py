import json
# json.dump = Gera um arquivo json
# json.load = converte dados do json para python
# pessoa = {
#     'nome': 'Mario',
#     'sobrenome': 'Cabral',
#     'enderecos': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ],
#     'altura': 1.7,
#     'numeros_preferidos': (2, 4, 6, 8, 0),
#     'dev': True,
#     'nada': None,
# }

# with open('pessoa.json', 'w', encoding='utf-8') as f_json:
#     json.dump(pessoa, f_json, ensure_ascii=False, indent=2)

with open('pessoa.json', 'r', encoding='utf-8') as f_json:
    pessoa = json.load(f_json)

print(pessoa)