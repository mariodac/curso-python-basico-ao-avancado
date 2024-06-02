# json.dump e json.load com arquivos
import json
import os


FILE_NAME = 'aula290.json'
ABSOLUTE_PATH_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), FILE_NAME))

string_json = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
'''
# loads -  para transformar string em json
movie = json.loads(string_json)
with open(ABSOLUTE_PATH_FILE, 'w') as file_:
    # dump - para transformar dicionario em arquivo.json
    json.dump(movie, file_, ensure_ascii=False, indent=2)

with open(ABSOLUTE_PATH_FILE, 'r') as file_:
    # load -  para transformar arquivo.json em dicionario
    movie_json = json.load(file_)
    print(movie_json)