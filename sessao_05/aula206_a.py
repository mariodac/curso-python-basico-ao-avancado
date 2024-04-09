# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados

# criando arquivo JSON com dados da classe
import json
PATH_FILE = 'data.json'
class Otaku:
    def __init__(self, name, favorite_serie, anime_watcher=False, manga_reader=False):
        self.name = name
        self.favorite_serie = favorite_serie
        self.anime_watcher = anime_watcher
        self.manga_reader = manga_reader

    def watch_anime(self):
        self.anime_watcher =True
        print(f'{self.name} está assistindo anime')

    def read_manga(self):
        self.manga_reader =True
        print(f'{self.name} está lendo manga')
        

if __name__ == '__main__':
    data = []
    otaku1 = Otaku('Jubileu', 'Naruto')
    otaku2 = Otaku('Irineu', 'Kakegurui')
    otaku1.watch_anime()
    otaku2.read_manga()
    data.append(otaku1.__dict__)
    data.append(otaku2.__dict__)
    with open(PATH_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)