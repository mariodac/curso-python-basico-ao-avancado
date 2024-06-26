# Exercicio
"""Desafios:

1. Leitura e Exibição de Dados de Clientes:

    Crie um programa que leia os dados de clientes de um arquivo CSV chamado clientes.csv.
    O arquivo contém as seguintes colunas: id_usuario, nome, email, cidade e estado.
    Exiba na tela as informações de cada cliente, formatadas em linhas e colunas.

2. Gravação de Novos Dados em um Arquivo CSV:

    Desenvolva um script que receba as informações de um novo cliente (nome, email, cidade e estado) do usuário.
    Armazene esses dados em um novo arquivo CSV chamado novos_clientes.csv.
    Utilize os mesmos cabeçalhos utilizados no arquivo clientes.csv.

3. Atualização de Registros em um Arquivo CSV:

    Elabore um programa que localize um cliente específico no arquivo clientes.csv a partir do seu email.
    Permita que o usuário altere as informações de cidade e estado do cliente encontrado.
    Salve as alterações no arquivo CSV original.

4. Cálculo de Estatísticas de Vendas:

    Crie um script que leia os dados de vendas de um arquivo CSV chamado vendas.csv.
    O arquivo contém as seguintes colunas: id_pedido, produto, quantidade, valor_unitario e valor_total.
    Calcule e exiba na tela as seguintes estatísticas:
        Total de vendas por produto
        Ticket médio (valor total das vendas / número de vendas)
        Produto com maior valor total vendido

5. Combinação de Dados de Múltiplos Arquivos CSV:

    Desenvolva um programa que combine as informações de dois arquivos CSV: clientes.csv e pedidos.csv.
    O arquivo usuarios.csv contém as colunas id_usuario, nome e email.
    O arquivo pedidos.csv contém as colunas id_pedido, id_usuario, data_pedido, valor_total.
    Gere um novo arquivo CSV chamado pedidos_completos.csv contendo as seguintes colunas:
        id_pedido
        nome_usuario (nome do usuário obtido a partir do id_usuario)
        data_pedido
        valor_total"""

import csv

