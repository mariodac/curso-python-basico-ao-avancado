# Exercicios
# Crie funções que duplicam, triplicam e quadruplicam
# o numero recebido como paramenro

def create_multiply(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply

duplicate = create_multiply(2)
triplicate = create_multiply(3)
quadruple = create_multiply(4)
quintuple = create_multiply(5)

print(duplicate(2))
print(triplicate(2))
print(quadruple(2))
print(quintuple(2))