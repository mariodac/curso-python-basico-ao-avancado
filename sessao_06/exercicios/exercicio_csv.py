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
    O arquivo contém as seguintes colunas: id_pedido, produto, quantidade, valor_unitario, valor_total, data_pedido.
    Calcule e exiba na tela as seguintes estatísticas:
        Total de vendas por produto
        Ticket médio (valor total das vendas / número de vendas)
        Produto com maior valor total vendido

5. Combinação de Dados de Múltiplos Arquivos CSV:

    Desenvolva um programa que combine as informações de dois arquivos CSV: clientes.csv e vendas.csv.
    O arquivo clientes.csv contém as colunas id_usuario, nome, email, cidade e estado.
    O arquivo vendas.csv contém as colunas id_pedido, id_usuario, data_pedido, valor_total, produto, quantidade, valor_unitario,.
    Gere um novo arquivo CSV chamado vendas_completos.csv contendo as seguintes colunas:
        id_pedido
        nome_usuario (nome do usuário obtido a partir do id_usuario)
        data_pedido
        valor_total"""

import csv
from pathlib import Path

def get_csv(filename:Path, mode:str):
    file_csv = open(filename, mode, encoding='utf-8', newline='')
    return file_csv

clientes_path = Path(__file__).parent / 'clientes.csv'
collumns_names = ['id_usuario', 'nome', 'email', 'cidade', 'estado']
# inicio exercicio 1
file_csv = get_csv(clientes_path, 'r')
reader = csv.DictReader(file_csv)
print(' | '.join(collumns_names))
for line in reader:
    print(f'{line['id_usuario']} | {line['nome']} | {line['email']} | {line['cidade']} | {line['estado']}')
    last_id = int(line['id_usuario'])
file_csv.close()
# fim exercicio 1

# inicio exercicio 2
# new_id = str(last_id+1)
# name = input('Digite o nome => ')
# email = input('Digite o email => ')
# city = input('Digite a cidade => ')
# estate = input('Digite o estado => ')
# client = {'id_usuario' : new_id, 'nome' : name, 'email' : email, 'cidade' : city, 'estado' : estate}
# file_csv = get_csv(clientes_path, 'a')
# writer = csv.DictWriter(file_csv, fieldnames=collumns_names)
# writer.writerow(client)
# file_csv.close()
# fim exercicio 2

# inicio exercicio 3
# email = input('Digte o email => ')
# file_csv = get_csv(clientes_path, 'r')
# reader = csv.DictReader(file_csv)
# list_reader = []
# not_found = True
# index = 0
# for line in reader:
#     list_reader.append(line)
#     if email == line['email']:
#         print(f'Cidade atual => {line['cidade']}')
#         city = input('Digite a cidade => ')
#         print(f'Estado atual => {line['estado']}')
#         estate = input('Digite o estado => ')
#         list_reader[index]['cidade'] = city
#         list_reader[index]['estado'] = estate
#         not_found = False
#     index += 1
# file_csv.close()
# if not_found:
#     print('Email não encontrado')
# file_csv = get_csv(clientes_path, 'w')
# writer = csv.DictWriter(file_csv, fieldnames=collumns_names)
# writer.writeheader()
# for line in list_reader: 
#     writer.writerow(line)
# file_csv.close()
# fim exercicio 3

# inicio exercicio 4
# venda_file = Path(__file__).parent / 'vendas.csv'
# file_csv = get_csv(venda_file, 'r')
# reader = csv.DictReader(file_csv)
# list_reader = [x for x in reader]
# total_qtd = 0
# total_value = 0
# sales_by_product = {}
# medium_ticket = 0
# most_value_total = 0
# most_value_product = ''
# for item_index, item in enumerate(list_reader):
#     total_qtd = int(item['quantidade'])
#     total_value = float(item['valor_total'].replace(',', '.'))
#     for new_item_index,new_item in enumerate(list_reader):
#         if item_index != new_item_index:
#             if item['produto'] == new_item['produto']:
#                 total_qtd += int(new_item['quantidade'])
#                 total_value += float(new_item['valor_total'].replace(',', '.'))
#         if total_value > most_value_total:
#             most_value_total = total_value
#             most_value_product = item['produto']
#         medium_ticket = total_value / total_qtd
#         sales_by_product.update({item['produto']:[total_qtd, medium_ticket]})
# for item in sales_by_product:
#     print(f'Total vendas do produto {item}: {sales_by_product[item][0]}')
#     print(f'Ticket médio do produto {item}: {sales_by_product[item][1]}')
#     print()
# print(f'O produto maior valor total vendido foi: {most_value_product}')
# file_csv.close()
# fim exercicio 4

# inicio exercicio 5
complete_sales = Path(__file__).parent / 'vendas_completos.csv'
file_clientes_csv = get_csv(clientes_path, 'r')
reader = csv.DictReader(file_clientes_csv)
list_clientes = []
collumns_names = ["id_pedido", "nome_usuario", "data_pedido", "valor_total"]