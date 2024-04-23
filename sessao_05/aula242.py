# Context Manager com função - Criando e usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(file_path, mode):
    try:
        print('Abrindo arquivo')
        file_ = open(file_path, mode, encoding='utf-8')
        yield file_
        print('Fechando arquivo')
        file_.close()
    except Exception as e:
        print('Ocorreu erro', e)
    finally:
        print('Fechando arquivo')
        file_.close()


with my_open('_aula.txt', 'w') as file_:
    file_.write('Olá mundo\n')
    file_.write('Linha 2\n')
    file_.write('Linha 3\n')
    file_.write('Linha 4\n', 123)