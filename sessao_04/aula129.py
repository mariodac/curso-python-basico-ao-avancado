# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm 
# Representados graficamente pelo diagrama de Venn 
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set (iterável) ou {1, 2, 3}

# Sets são eficientes para remover valores duplicados # de iteráveis.
# - eles não tem indexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) Itens presentes em ambos 
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^- Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^  s2
print(s3)