# Atributos de classe

class Pessoa:

    ano_atual = 2024
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        # se usar self, irá buscar primeiro na instancia da classe, se não encontrar na instancia pegara o atributo de classe
        # return self.ano_atual - self.age
        return Pessoa.ano_atual - self.age
    
p1 = Pessoa('Helena', 35)
p2 = Pessoa('João', 12)
# caso mude o valor do atributo de classe, pode causar erros em operações que depende desse atributo
Pessoa.ano_atual = 2
print(p1.get_birth_year())