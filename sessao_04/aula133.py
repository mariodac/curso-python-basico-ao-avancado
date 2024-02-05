# Função lambda em Python
# A função lambda é uma função como qualquer # outra em Python. Porém, são funções anônimas # que contém apenas uma linha. Ou seja, tudo # deve ser contido dentro de uma única
# expressão. 
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort()
# sorted(lista)
# python ordena utilizando a tabela unicode 

lista = [
  {'nome': 'Luiz', 'sobrenome': 'miranda'},
  {'nome': 'Maria', 'sobrenome': 'Oliveira'},
  {'nome': 'Daniel', 'sobrenome': 'Silva'},
  {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
  {'nome': 'Aline', 'sobrenome': 'Souza' }
]

def ordena(item):
    return item['nome']

def exibir(lista):
    for item in lista:
        print(item)
    print()

# lista.sort(key=ordena)

lista.sort(key=lambda item: item['nome'])

l1 = sorted(lista, key=lambda item: item['nome'])
l1 = sorted(lista, key=lambda item: item['sobrenome'])



