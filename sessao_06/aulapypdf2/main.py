# PyPDF2 - Para manipular arquivos PDF
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados dearquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2
# Doc: https://pypdf2.readthedocs.io/en/3.x/
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from PyPDF2 import PdfMerger
from os import listdir

ROOT_PATH = Path(__file__).parent
ORIGIN_PATH = ROOT_PATH / 'pdf_originais'
NEW_PATH = ROOT_PATH / 'arquivos_novos'

RELATORIO_PATH = ORIGIN_PATH / 'R20230210.pdf'
RELATORIO_PATH_2 = ORIGIN_PATH / 'R20240712.pdf'

NEW_PATH.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_PATH)

# quantidade de páginas
print(len(reader.pages))

# percorrer página do arquivo pdf
for page in reader.pages:
    print(page)

page0 = reader.pages[0]

# extrair texto da página 1
print(page0.extract_text())
# extrair primeira imagem do pdf
image0 = page0.images[0]
print(image0)
with open(NEW_PATH / image0.name, 'wb') as fp:
    fp.write(image0.data)

# escrevendo um novo pdf
writer = PdfWriter()
writer.add_page(page0)

with open(NEW_PATH / 'page0.pdf', 'wb') as fp:
    writer.write(fp)

# salvando cada página como um pdf
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(NEW_PATH / f'page{i+1}.pdf', 'wb') as fp:
        writer.add_page(page)
        writer.write(fp)

# unir dois arquivos pdf
merger = PdfMerger()
files = listdir(ORIGIN_PATH)
for file in files:
    merger.append(ORIGIN_PATH / Path(file))

with open(NEW_PATH / 'PDF_UNIDOS.pdf', 'wb') as fp:
    merger.write(fp)
