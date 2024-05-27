# namedtuples - tuplas imutáveis com nomes para valores
# Usamos nametuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As nametuples são imutáveis assim como as tuplas
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NameTuple

from collections import namedtuple
from typing import NamedTuple

class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


# Carta = namedtuple('Carta', ['valor', 'naipe'], defaults=['VALOR', 'NAIPE'])

as_espadas = Carta('A', '♠️')
print(as_espadas.naipe)
print()
print(as_espadas._fields)
print(as_espadas._field_defaults)
print()
print(as_espadas._asdict())
# for valor in as_espadas:
#     print(valor)