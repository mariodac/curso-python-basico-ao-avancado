import copy
from dados import produtos
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novo_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)]
for item in novo_produtos:
    for chave, valor in item.items():
        if chave == 'preco':
            item[chave] = valor * 1.1

produtos_ordenados_por_nome = sorted(produtos, key=lambda p: p['nome'])


produtos_ordenados_por_preco_reverse = sorted(produtos,reverse=True, key=lambda p: p['nome'])

produtos_ordenados_por_preco = sorted(produtos, key=lambda p: p['nome'])

print(novo_produtos)
print(produtos_ordenados_por_nome)
print(produtos_ordenados_por_preco_reverse)
print(produtos_ordenados_por_preco)

