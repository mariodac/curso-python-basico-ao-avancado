# Herança simples - Relações entre classes
# Associação - usa outro objeto, Agregação - tem outro objeto
# Composição - É dono de, Herança - É um

# Herança vs Composição

# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# builtins.object classe implicita do python
# Method resolution order - Ordem que é feita a busca de um método/atributo, primeiro busca na classe filha
# se não achar irá buscar nas classes pais
class Person:
    cpf = '1234'
    def __init__(self, first_name, last_name): 
        self.first_name = first_name
        self.last_name = last_name

    def say_class_name(self):
        print(self.first_name, self.__class__.__name__)

class Client(Person):
    ...

class Student(Person):
    cpf = 'blba'
    ...
        

c1 = Client('João', 'Otávio')
c1.say_class_name()
s1 = Student('Mario', 'Cabral')
s1.say_class_name()
print(c1.cpf)
print(s1.cpf)

help(Client)