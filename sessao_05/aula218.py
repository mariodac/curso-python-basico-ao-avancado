# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Car:
    def __init__(self, name):
        self._name = name
        self._motor = None
        self._manufacturer = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def manufacturer(self):
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

class Motor:
    def __init__(self, name):
        self._name = name
        self._car = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    def add_car(self, car):
        self._car.append(car)

    def list_cars(self):
        print(f"Carros com motor {self.name}")
        for car in self._car:
            print(car.name)

class Manufacturer:
    def __init__(self, name):
        self._name = name
        self._car = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    def add_car(self, car):
        self._car.append(car)

    def list_cars(self):
        print(f"Carros na fabricante {self.name}")
        for car in self._car:
            print(car.name)

motor1 = Motor('Pwered100')
motor2 = Motor('Turbo5k')

# ligação do carro com motor
car1 = Car('Uno')
car1.motor = motor1
motor1.add_car(car1)
car2 = Car('Cobalt')
car2.motor = motor2
motor2.add_car(car2)
car3 = Car('Toro')
car3.motor = motor2
motor2.add_car(car3) 



motor2.list_cars()
motor1.list_cars()

manufact1 = Manufacturer('Fiat')
manufact2 = Manufacturer('Chevrolet')

manufact1.add_car(car1)
car1.manufacturer = manufact1
manufact1.add_car(car3)
car3.manufacturer = manufact1
manufact2.add_car(car2)
car2.manufacturer = manufact2

manufact1.list_cars()
manufact2.list_cars()

print('#'*100)
print(f"Carro {car1.name} com motor {car1.motor.name} da fabricante {car1.manufacturer.name}")
print(f"Carro {car2.name} com motor {car2.motor.name} da fabricante {car2.manufacturer.name}")
print(f"Carro {car3.name} com motor {car3.motor.name} da fabricante {car3.manufacturer.name}")




