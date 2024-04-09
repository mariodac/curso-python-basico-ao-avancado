class Person:
    # inicializa atributos da classe
    # primeiro argumento de qualquer metodo da classe será self, não é necessário ser passado na chamada do método, 
    # Python irá passar esse self implicitamente
    # self referencia o objeto
    def __init__(self, first_name, last_name):
        ...
        self.first_name = first_name
        self.last_name = last_name

p1 = Person('Mario', 'Cabral') 
print(p1.last_name)