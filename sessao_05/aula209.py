# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe

class Pessoa:
    year = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def normal_class_method(self):
        print('Hey')

    @classmethod
    def class_method(cls):
        print('Hey')

    # factory method, metodo que cria um novo objeto com algo arbitrario ou alguma lógica
    # no factory method, não tem acesso a instância dentro desse metodo, pois é chamado a classe (cls) e não a instância (self)
    @classmethod
    def create_50_year(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def create_anonymous(cls, idade):
        return cls('Anônimo', idade)


p1 = Pessoa('João', 34)
p1.normal_class_method()
Pessoa.class_method()
# nesse exemplo utilizado para um caso precisa ser criado várias pessoas com 50 anos, 
# ou seja, vários objetos contendo um atributo com o mesmo valor
p2 = Pessoa.create_50_year('Maria')
p3 = Pessoa.create_anonymous(24)