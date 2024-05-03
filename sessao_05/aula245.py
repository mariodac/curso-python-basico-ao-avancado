# Método especial __call__
# callable é algo que pode ser executado com parêntes
# Em classes normais, __call__ faz a instância de uma
# classe "callable"

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwargs):
        print(*args, 'Chamando', self.phone)
        return 123

call1 = CallMe('23455234')
retorno_call = call1('Luiz Otávio')
print(retorno_call)