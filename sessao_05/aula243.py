# Funções decoradoras e decoradores com classes
def my_repr(self) -> str:
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr
def add_repr(cls):
    # def my_repr(self) -> str:
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'
    #     return class_repr
    cls.__repr__ = my_repr
    return cls

def my_planet(method):
    def intern(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if 'Terra' in result:
            return 'Você está em casa'
        return result
    return intern

class MyReprMixin:
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

@add_repr
class Team:
    def __init__(self, name):
        self.name = name

    

class Planet(MyReprMixin):
    def __init__(self, name):
        self.name = name

    @my_planet
    def says_name(self):
        return f'O nome do planeta é {self.name}'

# Team = add_repr(Team)
br = Team('Brasil')
pt = Team('Portugal')

earth = Planet('Terra')
mars = Planet('Marte')

print(br)
print(pt)

print(earth)
print(mars)

print(earth.says_name())
print(mars .says_name())
