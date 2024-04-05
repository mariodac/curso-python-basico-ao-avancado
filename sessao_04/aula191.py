# Problema dos parâmetros mutáveis em funções Python
# evitar utilizar parâmetros mutáveis em parâmetros com valor padrão, pois o valor vai sempre o mesmo, quando utilizar a função várias vezes


def add_clients(nome, list_clients=[]):
    list_clients.append(nome)
    return list_clients

# não foi gerado uma lista separada para cada variavel, pois o é parametro mutavel, será sempre o mesmo todas as vezes
client0 = add_clients('Ricardo')
client0 = add_clients('Neto', client0)
print(client0)

client01 = add_clients('Danilo')
client01 = add_clients('Geraldo', client01)
print(client01)

# forma de superar problema com parâmetros mutáveis
# cria uma lista para passar como argumento na função
list1 = []
client1 = add_clients('Mario', list1)
add_clients('Joana', client1)
print(client1)

client2 = add_clients('Helena')
add_clients('Douglas', client2)
print(client2)

# forma de evitar parâmetros mutáveis
def add_clients2(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


client3 = add_clients2('Fernando')
add_clients2('João', client3)
client3.append('Edu')

client4 = add_clients2('Madalena')
add_clients2('Jackson', client4)
print(client3)
print(client4)



