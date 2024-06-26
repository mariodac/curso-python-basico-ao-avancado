# csv.writer e csv.DictWriter
# csv.writer escreve o CSV em formato de lista
# csv.DictWriter lê o CSV em formato de dicionário

from pathlib import Path
import csv

PATH_CSV = Path(__file__).parent / 'aula294.csv'

list_clients = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'AV 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

collumns_names = list(list_clients[0].keys())
# with open(PATH_CSV, 'w', encoding='utf-8') as file_csv:
#     writer = csv.writer(file_csv)
#     writer.writerow(collumns_names)
#     for client in list_clients:
#         writer.writerow(client.values())

with open(PATH_CSV, 'w', encoding='utf-8', newline='') as file_csv:
    writer_dict = csv.DictWriter(file_csv, fieldnames=collumns_names)
    writer_dict.writeheader()
    for client in list_clients:
        writer_dict.writerow(client)
