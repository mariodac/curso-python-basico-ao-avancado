# recuperando dados de classe do JSON
import json
from aula206_a import PATH_FILE, Otaku

data = []
with open(PATH_FILE, 'r', encoding='utf-8') as file:
    data = json.load(file)
for d in data:
    otaku = Otaku(**d)
    print(otaku.name)
    print(otaku.favorite_serie)
