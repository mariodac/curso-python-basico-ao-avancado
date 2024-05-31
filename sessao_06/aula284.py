# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretórios atual (files).
# os.path.getsize e os.stat para dados dos arquivos

import os
from itertools import count


path_abs = os.path.abspath('.')
counter = count()
for root, dirs, files in os.walk(path_abs):
    the_counter = next(counter)
    print(the_counter)
    print(root)
    # print(dirs)
    # print(files)
    print()
    for dir_ in dirs:
        print('\t', the_counter, 'Dir:', dir_)

    for file_ in files:
        complete_path_file = os.path.join(root, dir_, file_)
        print('\t\t', the_counter, 'Files:', complete_path_file)
        # APAGA TODOS OS ARQUIVOS QUE TIVEREM NO DIRETORIOS E SUBDIRETORIOS DO CAMINHO INFORMADO
        # if not os.path.isdir(complete_path_file):
            # os.unlink(complete_path_file)