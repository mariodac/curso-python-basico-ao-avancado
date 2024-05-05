"""Este é um módulo de exemplo

Este módulo contém funções e exemplos de documentação de funções
"""

var_1 = 1

class Foo:
    """Esta é uma classe de exemplo

    Esta classe contém funções e exemplos de documentação de funções
    """
    # def sum_(x, y)
    def sum_(self,x: int | float, y: int | float) -> int | float:
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
            self,
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
    
    def bar(self) -> int:
        """O que o método faz
        
        :raises NotImplementedError: Se o método não for definido
        :raises ValueError: Se o valor for inválido
        """
        raise NotImplementedError('Error')

var_2 = 2
var_3 = 3
var_4 = 4