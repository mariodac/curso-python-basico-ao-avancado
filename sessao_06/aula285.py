# os.path.getsize e os.stat para dados dos arquivos

import os
from itertools import count
import math


path_abs = os.path.abspath('.')
counter = count()
def format_lenght(length_bytes: int, base:int = 1000) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""
    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0,0B.
    if length_bytes <= 0:
        return '0.0B'
    
    # tupla com os tamanhos
    #                       0    1     2      3     4     5 
    length_abbreviations = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do length_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso indice na abreviação dos tamanhos
    index_abbreviations_length = int(math.log(length_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto
    pow_ = base ** index_abbreviations_length
    # Tamanho final
    final_length = length_bytes / pow_
    # A abreviação que queremos
    length_abbreviation = length_abbreviations[index_abbreviations_length]
    return f'{final_length:.2f} {length_abbreviation}'

for root, dirs, files in os.walk(path_abs):
    if root.startswith('.'):
            continue
    the_counter = next(counter)
    print(the_counter)
    print(root)
    # print(dirs)
    # print(files)
    print()
    for dir_ in dirs:
        if dir_.startswith('.'):
            continue
        print('\t', the_counter, 'Dir:', dir_)

    for file_ in files:
        if file_.startswith('.'):
            continue
        complete_path_file = os.path.join(root, dir_, file_)
        stats = os.stat(complete_path_file)
        length = stats.st_size
        print('\t\t', the_counter, 'Files:', complete_path_file, format_lenght(length))
        