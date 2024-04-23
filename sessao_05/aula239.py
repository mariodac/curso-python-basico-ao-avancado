# __new__ e __init__ em classes Python, funciona como o construtor das outras linguagens
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls
# __new__  ❗DEVE retornar o novo objeto❗
# __init__ é o método responsável por inicializar
# a instância, Por isso, init recebe self
# __init__ ❗NÃO DEVE retornar nada (None)❗
# object é a super classe de uma classe
 
class A:

    def __new__(cls, *args, **kwargs):
        print('Antes de criar a instância')
        instance = super(A, cls).__new__(cls)
        instance.y = 213
        print('Depois de criar a instância')
        return instance
    def __init__(self, x) -> None:
        self.x = x
        print('Inicializando')

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'
a = A(345)
# maneira que o python faz implicitamente para instanciar uma classe
# a = object.__new__(A)
# a.__init__()
print(a)
a2 = A(678)
print(a2)