class Pessoa:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name