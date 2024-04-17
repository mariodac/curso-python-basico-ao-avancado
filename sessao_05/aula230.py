# Classes abastras - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instanciadas diretamente
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethods).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta
# É possível criar @property @property.setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno
# uma classe abstrata em Python deve ter pelo menos 1 metodo abstrato
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação

from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
      self._name = None
      self.name = name

    @property
    def name(self): 
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self, name): ...
    

class Foo(AbstractFoo):
    # name = ''
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')
    
    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name 

foo = Foo('Bar')
print(foo.name)