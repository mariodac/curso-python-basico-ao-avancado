# Context Manager com classes
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interassado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados
# O método __exit__ receberá classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será suprimidas.

# Ex:
# with open('_aula.txt', 'w') as file:
#     ...

class MyOpen:
    def __init__(self, file_path, mode):
        print('INIT')
        self.file_path = file_path
        self.mode = mode
        self._file = None
    def __enter__(self):
        print('ENTER. ABRINDO ARQUIVO')
        self._file = open(self.file_path, self.mode, encoding='utf-8')
        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        self._file.close()
        print('EXIT. FECHANDO ARQUIVO')
        # exception_.add_note('ERROU FEIO')

        # raise class_exception('Tá fazendo coisa errada ai')
        # raise class_exception(*exception_.args).with_traceback(traceback_)

        # print(class_exception)
        # print(exception_)
        # print(traceback_)

        # raise ConnectionError('Sem internet irmão')
    
        # return True # Tratei a exceção


# instance_ = MyContextManager()
with MyOpen('_aula.txt', 'w') as file_:
    print('WITH', file_)
    file_.write('ALGUMA COISA\n')
    file_.write('LINHA 2\n', 123)