# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base para a recursão
# - fatorial - n! = 5! =   * 4 * 3 * 2 * 1 = 120

def recursive(start=0, end=10):
    print(start)
    #  Caso base
    if start >= end:
        return end
    # Caso recursivo
    # contar até chegar ao final
    start += 1
    return recursive(start, end)

recursive()