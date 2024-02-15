# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se ____main_
# Você pode importar outro módulo inteiro ou parte do módulo 
# 0-python-conhece a pasta onde o ____main__ está e as pastas
# abaixo dele.s
# Ele não reconhece pastas e módulos acima do ____main___ por 
# padrão
# O python-conhece todos os módulos e pacotes presentes 
#nos caminhos de sys.path
try:
    import sys
    sys.path.append('C:/')
except ModuleNotFoundError:
    ...

import aula154_m

import modulo_python
 
print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')