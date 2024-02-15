from sys import path

import aula157_package.modulo
from aula157_package import modulo
from aula157_package.modulo import soma_do_modulo
from aula157_package.modulo import *

print(__name__)
print(*path, sep='\n')
print(aula157_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)

