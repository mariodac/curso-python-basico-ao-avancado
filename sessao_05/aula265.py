# dataclasses = O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo usuario
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple, field, fields

# argumento frozen impede que os atributos sejam setados
# com argumento init=False, post init não é chamado
# repr ativa/desativa o repr da classe
# valores padrões apenas para tipos imutáveis
@dataclass(order=True)
class Person:
    first_name: str
    last_name: str = field(default='MISSING')
    age: int = 18
    adresses: list[str] = field(default_factory=list)


    # def __init__(self, first_name, last_name, age):
    #     ...
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.age = age
    #     self.complete_name = f"{self.first_name} {self.last_name}"

    # post init não é chamado quando parametro init é false
    # def __post_init__(self):
    #     self.complete_name = f"{self.first_name} {self.last_name}"

    # @property
    # def complete_name(self):
    #     return f"{self.first_name} {self.last_name}"
    
    # @complete_name.setter
    # def complete_name(self, value):
    #     firstname, *sobrenome = value.split()
    #     self.first_name = firstname
    #     self.last_name = ' '.join(sobrenome)

if __name__ == '__main__':
    p1 = Person('Mario',)
    p2 = Person('Mario', 'Cabral', 30)
    print(p1)
    print(astuple(p1)[1])
    print(asdict(p1).get('age'))
    print(asdict(p1).items())
    # print(fields(p1))
    # list_person = [Person('A', 'Z', 30), Person('C', 'Y', 10), Person('B', 'X', 20)]
    # sorted_person = sorted(list_person, reverse=True)
    # print(sorted_person)
    # sorted_person_2 = sorted(list_person, reverse=False, key=lambda p: p.age)
    # print(sorted_person_2)
    # print(p1.complete_name)
    # p1.complete_name = 'João Batista Figueiredo'
    # print(p1)
    # print(p1 == p2)