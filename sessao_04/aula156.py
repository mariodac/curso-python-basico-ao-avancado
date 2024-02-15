import importlib

import aula156_m

for i in range(10):
    importlib.reload(aula156_m)
    print(i)

print('FIM')