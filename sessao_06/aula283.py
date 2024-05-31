# https://docs.python.org/3/library/os.html#os.listdir
# os.listdir para navegar em caminhos
# /User/username/Desktop/EXEMPLO (Linux, Mac)
# C:\Users\username\Desktop\EXEMPLO (Windows)

import os

path_abs = os.path.abspath('.')
path_items = os.listdir(path_abs)
print(path_items)

for item in path_items:
    complete_path = os.path.join(path_abs, item)
    if not os.path.isdir(complete_path):
        continue
    print(complete_path)
    for new_item in os.listdir(complete_path):
        print(new_item)