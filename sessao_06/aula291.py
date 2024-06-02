# Manipulando caminhos, pastas e arquivos no Python com pathlib
# Usamos a pathlib, para trabalhar com caminhos, pastas e arquivos de forma
# que um código funcione em Windows, Linux e Mac

from pathlib import Path
# retorna o caminho relativo
path_project = Path()
print('caminho relativo', path_project)
# para obter o caminho absoluto
print('caminho absoluto', path_project.absolute())

path_file = Path(__file__)
print('arquivo atual', path_file)
print('diretorio acima do arquivo atual', path_file.parent)
print('diretorio acima do diretorio acima do arquivo atual', path_file.parent.parent)

new_path = path_file.parent / 'nova_caminho'
print(new_path / 'arquivo.txt')

print('HOME', Path.home())
file_desktop = Path.home() / 'Desktop' / 'arquivo.txt'
# criando o arquivo, escrevendo e lendo
# file_desktop.touch()
# file_desktop.write_text('Olá mundo', encoding='utf-8')
# print(file_desktop.read_text())

# with file_desktop.open('a+') as file_txt:
#     file_txt.write('Uma linha\n')
#     file_txt.write('Outra linha\n')
# apagando arquivo
# file_desktop.unlink()

path_dir = Path.home() / 'Desktop' / 'Python top'
path_dir.mkdir(exist_ok=True)
sub_path = path_dir / 'Olá mundo'
sub_path.mkdir(exist_ok=True)
file_txt = sub_path / 'arquivo.txt'
file_txt.touch()
file_txt.write_text('Hey')

files = path_dir / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file_ = files / f'file_{i}.txt'

    if file_.exists():
        file_.unlink()
    else: 
        file_.touch()

        with file_.open('a+') as text_file:
            text_file.write(f'Arquivo {i}\n')

def rmtree(root: Path, remove_root=False):
    for file_item in root.glob('*'):
        if file_item.is_dir():
            print('DIR ', file_item )
            rmtree(file_item)
            file_item.rmdir()
        else:
            print('FILE ', file_item )
            file_item.unlink()
    if remove_root:
        root.rmdir()

rmtree(path_dir, True)



    



