# metho vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    # todo método que utiliza o self, é metodo de instância

    # setter
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        return ('LOG', msg)
    
def connection_log(msg):
    return ('LOG', msg)


c1 = Connection()
c1.set_user('mario')
c1.set_password('123')
print(c1.user, c1.password)

c2 = Connection.create_with_auth('mateus', '345')
print(c2.user, c2.password)


Connection.log('Isto é um log')