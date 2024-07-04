# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
ROOT_PATH = Path(__file__).parent
ZIP_DIR = ROOT_PATH / 'aula_304_diretorio_zip'
COMPRESSED_PATH = ROOT_PATH / 'aula_304_compactado.zip'
UNZIP_PATH = ROOT_PATH / 'aula_304_descompactado'

shutil.rmtree(ZIP_DIR, ignore_errors=True)
Path.unlink(COMPRESSED_PATH, missing_ok=True)
shutil.rmtree(str(COMPRESSED_PATH).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(UNZIP_PATH, ignore_errors=True)

# raise Exception('Arquivo apagados')

# Cria o diretório para a aula
ZIP_DIR.mkdir(exist_ok=True)

def create_files(qtd:int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as file_txt:
            file_txt.write(f'Texto do {texto}')

create_files(10, ZIP_DIR)

# Criando um zip e adicionando arquivos
with ZipFile(COMPRESSED_PATH, 'w') as zip_file:
    for root, dirs, files in os.walk(ZIP_DIR):
        for file_item in files:
            # cria o zip com a mesma estrutura de pastas do caminho original (inclui pastas e subspastas do usuário)
            # zip_file.write(os.path.join(root, file_item))
            # cria zip apenas com os arquivos
            zip_file.write(os.path.join(root, file_item), file_item)
# Lendo arquivos de um zip
with ZipFile(COMPRESSED_PATH, 'r') as zip_file:
    for file_item in zip_file.namelist():
        print(file_item)
# Extraindo arquivos de um zip
with ZipFile(COMPRESSED_PATH, 'r') as zip_file:
    # extrair tudo do zip
    zip_file.extractall(UNZIP_PATH)