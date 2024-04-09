# Métodos em instâncias de classes Python
class Car:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print(f'{self.name} acelerou')

fusca = Car('Fusca')
fusca.name = 'fusca' # hard coded, escrever valor diretamente na variável
print(fusca.name)
print(fusca.accelerate())