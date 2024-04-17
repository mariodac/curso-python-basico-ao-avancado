# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança Simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> Filelog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente (Pessoa, Filelog)

# Problema do diamante
# A, B, C, D
# D(B, C) - C(A) - B(A) - A

#       A
#     /   \
#    B     C
#     \   /
#       D
# Se caso D utilizar um método que está B e C, possuindo o mesmo nome, qual o método D irá pegar?
# Exemplo
# método -> falar -> A, B, C
# D não possui o método falar, nas versões do python 3.2 e superiores, é utilizado o algoritmo C3 superclass linearization para gerar a ordem de chamada dos métodos

# Python 3 usa C3 superclass linearization
# para gerar o mro.
# https://en.wikipedia.org/wiki/C3_linearization

# Para saber a ordem de chamada dos métodos
# Use o métidi de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)  


class A:
    ...
    def who_am_i(self):
        print('A')

class B:
    ...
    # def who_am_i(self):
    #     print('B')

class C(A):
    ...
    # def who_am_i(self):
    #     print('C')

# ordem da herança mudar o algoritmo do mro
class D(B, C):
    ...
    # def who_am_i(self):
    #     print('D')


d = D()
d.who_am_i()
print(D.__mro__)
print(D.mro())