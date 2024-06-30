# random tem geradores de números pseudoaleatórios 
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algoritmo,
# a saída poder ser previsível
# doc: https://docs.python.org/pt-br/3/library/random.html
import random
# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
random.seed(0)

# random.randrange(inicio, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
print("Numero inteiro aletório entre 10 e 20, com passo 2 => ", r_range)

# random.randint(inicio, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
# [a, b] -> inclui o a e b no intervalo
#   [] -> indica que o valor está incluído no intervalo
#  (a, b) -> não inclui o a e b no intervalo
#   () -> indica que o valor não está incluído no intervalo
r_int = random.randint(10, 20)
print('Numero inteiro aleatório sem passo =>', r_int)

# random.uniform(inicio, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_float = random.uniform(10, 20)
print('Numero flutuante aleatório sem passo =>', r_float)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['João', 'Luiz', 'Mario', 'Douglas', 'Victor', 'Manuel']
random.shuffle(nomes)
print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3)
print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))
