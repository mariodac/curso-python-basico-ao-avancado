# secrets gera números aleatóriso seguros
import secrets
import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))
# comando python para gerar senhas aleatórias
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"
random = secrets.SystemRandom()

# print(secrets.randbelow(100))
# print(secrets.choice([10, 20, 30, 40, 50]))

#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print('Numero inteiro aleatório sem passo =>', r_int)

#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_float = random.uniform(10, 20)
print('Numero flutuante aleatório sem passo =>', r_float)

#   -> Embaralha a lista original
nomes = ['João', 'Luiz', 'Mario', 'Douglas', 'Victor', 'Manuel']
random.shuffle(nomes)
print(nomes)

#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3)
print(novos_nomes)

#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
print(novos_nomes)

#   -> Escolhe um elemento do iterável
print(random.choice(nomes))