# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# Se um objeto precisa de outro objeto é agregação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralemente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa
# (existem controvérsias sobre as definições de agregação).

class ShoppingCart:
    def __init__(self):
        self._products = []

    def total(self):
        return sum([p.price for p in self._products])
    
    def listar_products(self):
        for product in self._products:
            print(product.name, product.price)

    def insert_products(self, *products):
        for product in products:
            self._products.append(product) 
        # self._products += products
        # self._products.extend(products)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = ShoppingCart()
p1, p2 = Product('Caneta', 1.20), Product('Camisa', 20)
cart.insert_products(p1, p2)
cart.listar_products()
print(cart.total())