# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemo seguir as seguintes converções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
#  __ (dois underlines) = private
#        "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#        só DEVE ser usado na classe em que foi declarado

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def public_method(self):
        return 'metodo publico'
    
    def _protected_method(self):
        return 'metodo protegido'
    
    def __private_method(self):
        return 'metodo privado'

f = Foo()
print(f.public)