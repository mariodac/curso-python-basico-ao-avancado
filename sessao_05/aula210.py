# @staticmethod (métodos estáticos) são inúteis em Python
#  Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua classe
# Basicamente protege o metodo com o namespace da classe
class Classe:
    @staticmethod
    def function(*args, **kwargs):
        print('Oi', args, kwargs)

def function(*args, **kwargs):
    print('Oi', args, kwargs)

c1 = Classe()
c1.function(1, 2, 3)
Classe.function(nomeado=1)
function(1, 2, 3)
function(nomeado=1)