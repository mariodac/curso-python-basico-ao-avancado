#string.Template para substituir variáveis em textos
# https://docs.python.org/pt-br/3.10/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template
import locale
import json
import string
from datetime import datetime
from pathlib import Path

FILE_PATH = Path(__file__).parent / 'aula298.txt'

locale.setlocale(locale.LC_ALL, '')

def convert_to_brl(numero: float | int) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=True, grouping=True)
    return brl

data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=convert_to_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)
# print(json.dumps(dados, indent=2, ensure_ascii=False))
texto = '''
Prezado(a) %nome,

Informamos que sua mensalidade será cobrada no valor de %{valor} no dia %data. Caso deseje cancelar o serviço, entre em contato com a %empresa pelo telefone %telefone.

Atenciosamente,

%{empresa},
Abraços
'''

class MyTemplate(string.Template):
    delimiter = '%'

template = MyTemplate(texto)
print(template.substitute(dados))

with open(FILE_PATH, 'r', encoding='utf-8') as file_txt:
    texto = file_txt.read()
    template = string.Template(texto)
    print(template.substitute(dados))