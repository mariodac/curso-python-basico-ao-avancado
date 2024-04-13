# super() é a super classe na sub classe
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class MyString(str):
    # sobrepor totalmente o metodo 
    # def upper(self):
    #     return 'ABC'
        
    # 
    def upper(self):
        print('TAREFA ANTES D UPPER')
        string = super().upper()
        print('TAREFA DEPOIS D UPPER')
        return string

class A:
    def __init__(self, name):
        self.name = name
    attribute_a = 'valor a'
    def method(self):
        print('A')

class B(A):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)
    attribute_b = 'valor b'
    def method(self):
        print('B')

class C(B):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Sistema burlado')
    attribute_c = 'valor c'
    # recomendao utilizar o super
    def method(self):
        A.method(self)
        super().method()
        super(B, self).method()
        print('C')

c = C('atributo', 13)
print(C.mro())
c.method()

# string = MyString('Mario')
# print(string.upper())