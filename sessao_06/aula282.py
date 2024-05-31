# https://docs.python.org/3/library/os.path.html#module-os.path
# os.path trabalha com caminhos em Windows, Linux e Mac
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esse sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2/arquivo.txt' no Windows
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemoplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.

import os

path_ = os.path.join('c:', '/home/user', 'Desktop', 'arquivo.txt')
# print(path_)
# divide o caminho informado em dois, usando a ultima barra como separador
directory, file_ = os.path.split(path_)
# obtem caminho, extensão do arquivo
# file_directory, extension_file = os.path.splitext(file_)
# obtem a letra do disco (windows)
# disk_drive, path_drive = os.path.splitdrive(path_)
# print(disk_drive, path_drive)
# print(file_directory, extension_file)
# print(directory, file_)
# verifica se o caminho existe
# print(os.path.exists(path_))
# caminho absoluto
# print(os.path.abspath('.'))
# obtem o basename do caminho, a parte final do caminho
print(os.path.basename(path_))


