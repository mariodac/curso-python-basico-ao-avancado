# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem
# User todos os valores da menor lista
# Ex.:
# ['Salvador', 'Ubatuba','Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(list1, list2):
    new_zipper = []
    if len(list1) < len(list2):
        min_list = list1
        new_zipper = make_zip(min_list, list2)
    else:
        min_list = list2
        new_zipper = make_zip(min_list, list1)
    return new_zipper

def make_zip(min_list, other_list):
    new_zipper = []
    for index in range(len(min_list)):
        new_zipper.append((min_list[index], other_list[index]))
    return new_zipper
    



list1 = ['Salvador', 'Ubatuba','Belo Horizonte']
list2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(list1, list2))