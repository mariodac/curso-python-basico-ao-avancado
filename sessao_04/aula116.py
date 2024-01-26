"""
Closure e funções que retornam outras funções
"""

def create_greeting(message):
    def greet(name):
        return f'{message}, {name}!'
    return greet


good_morning = create_greeting('Bom dia')
good_evening = create_greeting('Boa noite')

print(good_morning)
print(good_evening('Maria'))

nomes = ['João', 'Marcelo', 'Luiz']

for nome in nomes:
    print(good_morning(nome))
    print(good_evening(nome))