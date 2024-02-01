# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

p1 = {
    'nome': 'Mário',
    'sobrenome': 'Cabral',
    'idade': 18,
}

nome = p1.pop('nome')
print(nome)
print(p1)

ultima_chave = p1.popitem()
print(nome)
print(p1)

p1.update({
    'nome': nome,
    'idade': 29,
})
print(p1)
p1.update(nome='João', idade=28)
print(p1)

tupla = (('nome', 'julio'), ('idade', 25))
p1.update(tupla)
print(p1)

lista = [['nome', 'Marian'], ['idade', 30]]
p1.update(lista)
print(p1)
