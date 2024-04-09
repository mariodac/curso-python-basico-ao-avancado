# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para noms de classes.

# string = 'Mario' # instância de str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    ...

p1 = Pessoa() # gerando uma instancia da classe Pessoa
# inicializando atributos para esta instância de Pessoa
p1.nome = 'Mario' 
p1.sobrenome = 'Cabral'
print(p1)