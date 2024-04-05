# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
import os

path_file = r'arquivo.txt'
with open(path_file, 'w', encoding='utf-8') as file:
    file.write('Olá mundo')

os.rename(path_file, 'arquivo2.txt')
# os.unlink(path_file)