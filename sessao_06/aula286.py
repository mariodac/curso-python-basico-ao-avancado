# os + shutil - Copiando arquivos com Python
# os + shutil - Apagando e copiando pastas com Python
# Vamos copiar arquivos de uma pasta para outra
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

def create_path(path_root: str) -> str: 
    dir1 = os.path.join(path_root, 'teste')
    complete_path = dir1
    os.makedirs(dir1, exist_ok=True)
    open(os.path.join(dir1, 'arquivo1.txt'), 'w').close()
    dir2 = os.path.join(dir1, 'pasta')
    os.makedirs(dir2, exist_ok=True)
    open(os.path.join(dir2, 'arquivo2.txt'), 'w').close()
    dir3 = os.path.join(dir2, 'subpasta')
    os.makedirs(dir3, exist_ok=True)
    open(os.path.join(dir3, 'arquivo3.txt'), 'w').close()
    dir4 = os.path.join(dir3, 'subsubpasta')
    os.makedirs(dir4, exist_ok=True)
    open(os.path.join(dir4, 'ultimo_arquivo.txt'), 'w').close()
    return complete_path

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
ORIGINAL_PATH = create_path(DESKTOP)
NEW_PATH = os.path.join(DESKTOP, 'PASTA')
# print(HOME)
# print(os.listdir(DESKTOP))
os.makedirs(NEW_PATH, exist_ok=True)
if os.path.exists(NEW_PATH):
    shutil.rmtree(NEW_PATH)
# copia tudo o que está em um pasta e cria pasta e cola nesta pasta, se nova pasta existir resultará em erro
shutil.copytree(ORIGINAL_PATH, NEW_PATH)

shutil.move(NEW_PATH, NEW_PATH + '_tabao')

# Método mais longo, mas permite mais liberdade para realizar operações
# for root, dirs, files in os.walk(ORIGINAL_PATH):
#     for dir_ in dirs:
#         path_dir = os.path.join(root, dir_)
#         path_new_dir = os.path.join(root.replace(ORIGINAL_PATH, NEW_PATH), dir_)
#         os.makedirs(path_new_dir, exist_ok=True)
#     for file_ in files:
#         path_file = os.path.join(root, file_)
#         path_new_file = os.path.join(root.replace(ORIGINAL_PATH, NEW_PATH), file_)
#         shutil.copy(path_file, path_new_file)
