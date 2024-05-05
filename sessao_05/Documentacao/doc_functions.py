"""Este é um módulo de exemplo

Este módulo contém funções e exemplos de documentação de funções
"""

var_1 = 1

# def sum_(x, y)
def sum_(x: int | float, y: int | float) -> int | float:
    """Soma x e y

    A função soma você já conhece bastante

    :param x: O primeiro valor
    :type x: int or float
    :param y: O segundo valor
    :type y: int or float

    :return: A soma de x e y
    rtype: int or float
    """
    return x + y

def multiple(
        x: int | float,
        y: int | float,
        z: int | float | None = None
)-> int | float:
    """Multiplica x, y e/ou z

    Multiplica x e y. Se z for enviado, multiplica x, y, z.
    """
    if z is not None:
        return x * y
    return x * y * z

var_2 = 2
var_3 = 3
var_4 = 4