# Exercicio - Adiando execução de funções


def add(x, y):
    return x + y

def multiple(x, y):
    return x * y

def execute(function, x):
    def inside(y):
        return function(x, y)
    return inside

sum_five = execute(add, 5, 1)
multiple_ten = execute(multiple, 10, 1)
print(sum_five(10))
print(multiple_ten(10))