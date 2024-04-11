# Relações entre classes: associação, agregação e composição
# Composição é uma especialização de agregação.
# Se um objeto gerencia o ciclo de vida de outro objeto é composição
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são apagadas

class Client:
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def __del__(self):
        print('APAGANDO', self.name)

    def add_address(self, street, number):
        self.addresses.append(Address(street, number))

    def add_address_external(self, address):
        self.addresses.append(address)

    def list_addresses(self):
        for address in self.addresses:
            print(address.street, address.number)

class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __del__(self):
        print('APAGANDO', self.street, self.number)


cliente1 = Client('Mario')
cliente1.add_address('Av Brasil', 74)
cliente1.add_address('Rua B', 14)
address = Address('Rua da Paz', 88)
cliente1.add_address_external(address)
cliente1.list_addresses()
del cliente1

print('#'*10,'ENCERRADO', '#'*10)
