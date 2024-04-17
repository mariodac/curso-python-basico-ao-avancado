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
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno
# uma classe abstrata em Python deve ter pelo menos 1 metodo abstrato
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação

from abc import ABC, ABCMeta, abstractmethod

# forma 1 de criar uma classe abstrata
# class Log(metaclass=ABCMeta):
#     ...

# forma 2 de criar uma classe abstrata
class Log(ABC):
    # o método abstrato é FORÇADO, portanto DEVE ser implamentado em toda classe que herdar a classe abstrata
    @abstractmethod
    def _log(self, msg): ...
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')
    
class LogPrintMixin(Log):
    # para sobrepor um método deve ter a mesma assinatura
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

l = LogPrintMixin()
l.log_error('eita')