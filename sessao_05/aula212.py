# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo 🤯🤯🤯
# o property faz o metodo funcionar como um atributo da classe
# Geralmente é usada nas seguintes situações:
# - como getter
#  - p/ evitar quebrar código cliente
#  - p/ habiliar setter
#  - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Pen:
    def __init__(self, color):
        self.ink_color = color


    def get_color(self):
        print('GET COR')
        return self.ink_color
    
    # metodo pythonico
    @property
    def color(self):
        print('PROPERTY')
        return self.ink_color
    
    @property
    def material(self):
        return 'Plastico'



pen = Pen('Azul')
print(pen.get_color( ))
print(pen.color)
print(pen.material)