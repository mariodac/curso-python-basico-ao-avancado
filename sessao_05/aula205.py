# __dict__  e vars para atributos de instancia
# mantem o objeto do tipo mapping
# um dicionario que está dentro do objeto, mantem os valores que podem ser escritos nesse objeto

class Pessoa:

    ano_atual = 2024
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        return Pessoa.ano_atual - self.age
    
p1 = Pessoa('Helena', 35)
dados = {'name': 'João', 'age': 35}
p2 = Pessoa(**dados)
print(p2.__dict__)
# print(p1.name)
# p1.name = 'Eita'
print(p1.name)
# __dict__ é editavel
# del p1.__dict__['name']
print(p1.__dict__)
print(vars(p1))