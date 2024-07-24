#  sys.argv - Executando arquivos com argumentos no sistema

import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
    except IndexError:
        print('Faltam argumentos')