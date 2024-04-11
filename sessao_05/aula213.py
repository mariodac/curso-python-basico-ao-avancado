# @property + @setter - getter e setter no modo Pythônico
# - como getter
#  - p/ evitar quebrar código cliente
#  - p/ habiliar setter
#  - p/ executar ações ao obter um atributo

class Pen:
    def __init__(self, color):
        self.ink_color = color
        # convenção em python, atributo iniciado "_" ou "__" não deve ser usado fora da classe, ele é protegido, interno da classe
        # basicamente funciona como private protect de outras linguagens
        self._color = self.ink_color
        self.color = color
        self._material = None
    @property
    def color(self):
        print('GETTER')
        return self.ink_color
    # o setter tem a vantagem de restringir valores
    @color.setter
    def color(self, value):
        print('SETTER', value)
        self.ink_color = value

    @property
    def material(self):
        return self._material
    
    @material.setter
    def material(self, material_name):
        self._material = material_name
        

pen = Pen('Azul')
print(pen.color) 
# setter atribui valor
pen.color = 'Vermelho'
# getter -> obter valor
print(pen.color) 
pen.material = 'Plastico'
print(pen.material) 
