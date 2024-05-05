# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de um classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclasss)
# type('Name', (Bases,), __dict__)

# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução

# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)

# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
#  não precisa (as pessoas que realmente precisam de uma explicação
# sobre o porquê)."
# - Tim Peters (CPython Core Developer)
# ----- AULA 247
# objeto acima
# class Foo:
#     ...

# Foo =  type('Foo', (object,), {})
# f = Foo()
# print('f -> Foo()', isinstance(f, Foo))
# print(type(f))
# print(type(Foo))


# ----- AULA 248 e 249

from typing import Any


def my_repr(self):
    return f'{type(self).__class__.__name__}({self.__dict__})'

class Meta(type):
    # cria e retorna a classe na metaclasse
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = my_repr

        print(cls.__dict__)

        if 'speak' not in cls.__dict__ or not callable(cls.__dict__['speak']):
            raise NotImplementedError('Implemente speak')


        return cls
    
    # criar e retornar a instância
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        if 'name' not in instance.__dict__:
            raise NotImplementedError('Crie o attr name')
        print(instance.__dict__)
        return instance
        

class Person(object, metaclass=Meta):
    # speak = 123
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name):
        print('MEU INIT')
        self.name = name

    def speak(self):
        print('Falando')


p1 = Person('Mario')
print(p1)
print(p1.attr)
print(Person.attr)
