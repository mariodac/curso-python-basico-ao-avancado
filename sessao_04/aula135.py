#Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)

person = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}


data_person = {
    'idade': 16,
    'altura': 1.6,
}

complete_person = {**person, **data_person}
print(complete_person)

""" (a1, a2), b = person.items()
print(a1, a2, b)

c, d = person
print(c, d)

e, f = person.values()
print(e, f)

for chave, valor in person.items():
    print(chave, valor) """

def show_keyword_arguments(*args, **kwargs):
    print('NÃO NOMEADOS', args)

    for key, val in kwargs.items():
        print(key, val)

# show_keyword_arguments(1, 2, nome='Joana', id=123)
# show_keyword_arguments(**complete_person)

configs = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

show_keyword_arguments(**configs)

# args e kwargs
# args (já vimos)
#kwargs - keyword arguments (argumentos nomeados)