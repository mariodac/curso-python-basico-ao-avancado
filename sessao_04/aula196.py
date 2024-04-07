# Contralando a quantidade de argumentos posicionais e nomeados em funções
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗APENAS❗ posicional
# PEP 570 - Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Parameters (*) - * sozinho ❗NÃO SUGA❗ valores
# PEP 3102 - Keyword-Only Parameters
# https://peps.python.org/pep-3102/

# a e x não pode ser usado como argumento nomeado
def soma(a, x, /, b, y):
    print(a + x + b + y)

soma(1, 2, y = 3, b = 4)

# após * deve ter pelo um argumento
# tudo antes do * é argumento posicional
# tudo depois do * é argumento nomeado e não pode ser usado como argumento posicional
def multiplica(a, b, *, c):
    print(a * b * c)

multiplica(1, 2, c = 3)

# ambos / e * podem ser utilizados juntos
def divide(a, b, /, *, c):
    print(a / b / c)






