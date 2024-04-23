# open é classe de TextIOWrapper
path_file = r'_arquivo.txt'
with open(path_file, 'w+') as file:
    file.write('Hello World!\n')
    file.write('Olá mundo!\n')
    file.writelines(('Linha 3\n', 'Linha 4\n'))
    file.seek(0, 0)
    print(file.read())
    print('Lendo linha')
    file.seek(0, 0)
    print(file.readline(), end='')
    print(file.readline().strip())
    print('Lendo linhas')
    for line in file.readlines():
        print(line.strip())
print('#' * 10)
with open(path_file, 'r', encoding='utf-8') as file:
    print(file.read())