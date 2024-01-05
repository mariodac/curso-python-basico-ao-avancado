"""
Iterando strings com while
"""

nome = 'Mário Douglas'
indice = 0
nova_string = ''
while indice < len(nome):
    nova_string += f'={nome[indice]}'
    indice += 1

print(nova_string)