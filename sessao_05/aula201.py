# Entendendo self em classes Python
# palavra self é utilizada por convenção, para referenciar o próprio objeto
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias
# Na classe o self é a própria instância.
class Car:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print(f'{self.name} acelerou')

fusca = Car('Fusca')
Car.accelerate(Car('Celta'))
Car.accelerate(fusca)
print(fusca.name)
print(fusca.accelerate())