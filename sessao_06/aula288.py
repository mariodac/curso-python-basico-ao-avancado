"""# O que é JSON - JavaScript Object Notation
# JSON -  JavaScript Object Notation (extensão .json)
# É uma estrutura de daddos que permite a serialização
# de objetos em texto simples para facilitar a transmissão de
# dados através da rede, APIs web ou outros meios de comunicação.
# O JSON suporta os seguintes tipos de dados:
# Números: podem ser inteiros ou com ponto flutuante, como 42 ou 3.14
# Strings: são cadeias de caracteres, como "Olá, mundo!" ou "12345"
#   As strings devem ser envolvidas por aspas duplas
# Booleanos: são os valores verdadeiro (true) ou falso (false)
# Arrays: são listas ordenadas de valores, como [1, 2, 3] ou
#   ["Oi", "Olá", "Bom dia"]
# Objetos: são conjuntos de pares chave/valor -> {"nome": "João", "idade": 39}
# null: é um valor especial que representa ausência de valor

#json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null"""

import json
from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float

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
# print(string_json)
# loads -  para transformar string em json
movie: Movie = json.loads(string_json)
# pprint(movie, width=40)
# print(movie['title'])
# print(movie['characters'][0])
# tipagem auxilia pois identifica operações não suportadas pelo tipo
# print(movie['budget'] + 10)
# print(movie['year'] + 10)
# dumps - para transformar json em string
json_string = json.dumps(movie, ensure_ascii=False, indent=2)
print(json_string)
