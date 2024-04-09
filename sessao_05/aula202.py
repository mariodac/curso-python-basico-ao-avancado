# Escopo da classe e de métodos da classe
# a class possui seu prório escopo (name espace)

class Animal:
    nome = 'Macaco'

    def __init__(self, name):
        self.name = name
        variavel = 'valor'
        print(variavel)

    def eat(self, food):
        return (f'{self.name} está comendo {food}')
    
    # com self pode obter o atributo/método da classe mesmo estando num escopo diferente    
    def execute(self, *args, **kwargs):
        return self.eat(*args, **kwargs)

leao = Animal(name='Leão')
print(leao.nome)
print(leao.name)
print(leao.execute('Carne'))