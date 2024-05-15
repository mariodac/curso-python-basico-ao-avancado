# Enum -> Enumerações
# Enumeração na programação, são usadas em ocasiões onde temos
# um determinado número de coisas.
# Enums têm membros e seus valores são constantes
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
# diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coias relacionadas com tipo
# Para obter os dados:
# membro = Classe(valor), Classe['chave]
# chave = Classe.chave.name
# valor - Classe.chave.value
import enum

# Directions = enum.Enum('Directions', ['LEFT', 'RIGHT', ])

class Directions(enum.Enum):
    LEFT = 1
    RIGHT = enum.auto()
    UP = 'ACIMA'
    DOWN = 'ABAIXO'

print(Directions(1), Directions['RIGHT'], Directions.LEFT)
print(Directions(1).name, Directions.LEFT.value)


def move(direction:Directions):
    if not isinstance(direction, Directions):
        raise ValueError(f'Direção inválida: {direction}')
    print(f'Movendo para {direction.name} ({direction.value})')


move(Directions.LEFT)
move(Directions.RIGHT)
move(Directions.UP)
# move('acima')