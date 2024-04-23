# Criando arquivos com Python
# Usamos a função open para abrir
# um arquivo em Pyhon (ele pode ou não existir)
# Modos:
# r (leitura), w (escria), x (para criação)
# a (escreve ao final, append mode), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobbre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

path_file = '_arquivo.txt'

file = open(path_file, 'w')

file.close()

# context manager
with open(path_file, 'w') as file:
    print('Olá mundo')
    print('Aquivo vai ser fechado')